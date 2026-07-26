"""Modernized rewrite of David Bombal's paramiko-pythonssh1.py.

Original (Python 2):
    https://github.com/davidbombal/pythonvideos/blob/master/paramiko-pythonssh1.py

Same end result as the original -- two loopbacks, OSPF, and VLANs 2-20 on a
Cisco IOS device -- but written for Python 3.12 with runtime credentials,
error handling, and prompt-based synchronization instead of fixed sleeps.

Usage:
    export NET_HOST=192.168.122.72
    export NET_USER=david
    python paramiko_ssh_modern.py
"""

import os
import sys
import time
from getpass import getpass

import paramiko

# --- Connection settings ---------------------------------------------------

HOST = os.environ.get("NET_HOST", "192.168.122.72")
PORT = int(os.environ.get("NET_PORT", "22"))

CONNECT_TIMEOUT = 10.0
READ_TIMEOUT = 15.0

# GNS3 lab devices get rebuilt constantly, so their host keys change every time.
# Set this to False for any device you do not personally control.
LAB_MODE = True


class PromptTimeout(Exception):
    """Raised when a device stops responding mid-session."""


# --- Helpers ---------------------------------------------------------------


def get_credentials() -> tuple[str, str]:
    """Pull credentials from the environment, prompting for anything missing."""
    username = os.environ.get("NET_USER") or input("Username: ")
    password = os.environ.get("NET_PASS") or getpass("Password: ")
    return username, password


def read_until_prompt(channel, timeout: float = READ_TIMEOUT) -> str:
    """Read from the channel until the device sends a prompt ending in > or #.

    This replaces the original's time.sleep() guessing. Instead of hoping the
    device finished in half a second, we wait for it to say so.
    """
    buffer = ""
    deadline = time.monotonic() + timeout

    while time.monotonic() < deadline:
        if channel.recv_ready():
            # recv() returns bytes; decode before treating it as text.
            buffer += channel.recv(65535).decode("utf-8", errors="replace")
            if buffer.rstrip().endswith((">", "#")):
                return buffer
        else:
            time.sleep(0.05)

    raise PromptTimeout(f"No prompt after {timeout}s. Partial output:\n{buffer}")


def send_command(channel, command: str) -> str:
    """Send one command and return everything the device sends back."""
    channel.send(command + "\n")
    return read_until_prompt(channel)


def build_config_commands() -> list[str]:
    """Build the full command list before sending anything.

    Separating what to send from the act of sending it makes the config
    reviewable, testable, and reusable against another transport.
    """
    commands = [
        "configure terminal",
        "interface loopback 0",
        "ip address 1.1.1.1 255.255.255.255",
        "interface loopback 1",
        "ip address 2.2.2.2 255.255.255.255",
        "router ospf 1",
        "network 0.0.0.0 255.255.255.255 area 0",
        "exit",
    ]

    for vlan_id in range(2, 21):
        commands.append(f"vlan {vlan_id}")
        commands.append(f"name Python_VLAN_{vlan_id}")

    commands.append("end")
    return commands


def build_ssh_client() -> paramiko.SSHClient:
    """Create an SSHClient with a host key policy appropriate to the context."""
    client = paramiko.SSHClient()

    if LAB_MODE:
        # Accepts any host key without verification -- fine for a throwaway
        # lab, a man-in-the-middle opportunity anywhere else.
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    else:
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.RejectPolicy())

    return client


# --- Main ------------------------------------------------------------------


def main() -> int:
    username, password = get_credentials()
    ssh_client = build_ssh_client()

    try:
        # The context manager closes the session even if something raises.
        with ssh_client:
            ssh_client.connect(
                hostname=HOST,
                port=PORT,
                username=username,
                password=password,
                timeout=CONNECT_TIMEOUT,
                look_for_keys=False,
                allow_agent=False,
            )
            print(f"Connected to {HOST}")

            channel = ssh_client.invoke_shell()
            channel.settimeout(READ_TIMEOUT)

            read_until_prompt(channel)                  # drain the login banner
            send_command(channel, "terminal length 0")  # disable --More-- paging

            for command in build_config_commands():
                print(send_command(channel, command), end="")

    except paramiko.AuthenticationException:
        print(f"Authentication failed for {username}@{HOST}", file=sys.stderr)
        return 1
    except paramiko.SSHException as exc:
        print(f"SSH negotiation failed: {exc}", file=sys.stderr)
        return 1
    except PromptTimeout as exc:
        print(f"Device stopped responding: {exc}", file=sys.stderr)
        return 1
    except TimeoutError as exc:
        # Must be caught before OSError -- TimeoutError is a subclass of it.
        print(f"Timed out connecting to {HOST}:{PORT} - {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Could not reach {HOST}:{PORT} - {exc}", file=sys.stderr)
        return 1

    print("Configuration complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
