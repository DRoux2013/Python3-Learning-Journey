from napalm import get_network_driver
IP_ADDRESS = '10.10.10.1'
username = 'vyos'
password = 'vyos'
driver = get_network_driver('vyos')
device = driver(IP_ADDRESS, username, password)
device.open()
facts = device.get_facts()
interfaces = device.get_interfaces()
print(facts)
print(interfaces)
device.close()
