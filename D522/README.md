# Python3-Learning-Journey
My Initial Steps into Pyhton

**07/29/26:** Several weeks on and I've forgotten about this README. 
NAPALM lab issue, not sure what went wrong or if this by design, but numerous steps to get the lab working correctly and in the end, it froze. Steps are recorded for posterity. 

# 1. Fixed script logic — instantiate driver, then .open(), then call getters, then .close()

# 2. Fixed filename shadowing — renamed napalm.py to napalm_lab.py (was shadowing the real library)

# 3. Cleared stale bytecode / leftover file
rm /home/student/napalm.py
rm -rf /home/student/__pycache__

# 4. napalm wasn't installed system-wide — needed a venv (Ubuntu 24 externally-managed pip)

# 5. Installed python3-venv (mirror was stale, needed update first)
sudo apt-get update
sudo apt install python3.12-venv

# 6. Created and activated venv
python3 -m venv venv
source venv/bin/activate

# 7. Installed napalm + vyos driver in venv
pip install napalm
pip install napalm-vyos

# 8. Fixed missing pkg_resources — newer setuptools dropped it
pip install "setuptools==80.9.0"

# 9. GOTCHA: always run "python script.py" (no path) with (venv) active
#    /usr/bin/python bypasses the venv every time

# 10. NEXT SESSION: NetmikoTimeoutException - TCP connection failed
#     Need to complete GNS3 Network Startup, confirm VyOS booted + SSH reachable
python /home/student/napalm_lab.py

**Update 07/30/26:**
Root cause: napalm-vyos's interface-state parser (`vyos.py` line ~337)
expects a `show interfaces` output format that doesn't match this VyOS
build (2025.07.13-0023-rolling). This is a driver/library compatibility
bug, not a config or script error.

- Attempted downgrading `napalm-vyos` — failed to build from source in
  this environment (`ModuleNotFoundError: No module named 'pip'` inside
  the isolated build sandbox). Not worth pursuing further.
- **Resolution:** wrap `get_interfaces()` in a try/except to fail
  gracefully instead of crashing, and still demonstrate working
  `get_facts()` output.

## Status
Script runs cleanly end-to-end: connects, retrieves and prints facts,
attempts interfaces, catches the known driver bug, closes the connection.
No unhandled exceptions.

## Follow-up
- Note this as feedback for the course (napalm-vyos incompatibility with
  current VyOS rolling build) — candidate for `D522_Course_Feedback_Draft.md`
- Confirm with PA rubric whether interface data output is a hard
  requirement, or facts + graceful error handling is sufficient