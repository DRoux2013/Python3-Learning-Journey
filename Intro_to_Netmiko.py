from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios', 
    'ip': '10.10.10.10',
    'username': 'test',
    'password': 'password',
    'port': 8022,
    'secret': 'secret',
    'verbose': False,
}