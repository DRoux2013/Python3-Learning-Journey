from napalm import get_network_driver
#python3 -m venv venv
#source venv/bin/activate
#pip install napalm
#pip install napalm-vyos
IP_ADDRESS = '10.10.10.1'
username = 'vyos'
password = 'vyos'
driver = get_network_driver('vyos')
device = driver(IP_ADDRESS, username, password)
device.open()
facts = device.get_facts()
print(facts)
try:
    interfaces = device.get_interfaces()
    print(interfaces)
except Exception as e:
    print(f"get_interfaces() failed to due to a napalm-vyos driver bug: {e}")
device.close()