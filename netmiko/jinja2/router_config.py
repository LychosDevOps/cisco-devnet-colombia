from jinja2 import FileSystemLoader, Environment
from netmiko import ConnectHandler
import json
import time

template_dir = FileSystemLoader('templates')
template_env = Environment(loader=template_dir)
template_int_config = template_env.get_template('ospf.j2')
devices_data = { 
          'C8K1' : { 'interfaces':
            [
                {
                    'name': 'Loopback1',
                    'ip': '192.168.0.100',
                    'netmask': '255.255.255.255'
                },
                {
                    'name': 'GigabitEthernet2',
                    'ip': '172.16.0.1',
                    'netmask': '255.255.255.252'
                }
            ],
            'router':
                {
                    'protocol': 'ospf',
                    'id': '1',
                    'routerid': '1.1.1.1',
                    'area': '0' 
                }
        },
        'C8K2' : { 'interfaces':
        [
            {
                'name': 'Loopback1',
                'ip': '192.168.0.101',
                'netmask': '255.255.255.255'
            },
            {
                'name': 'GigabitEthernet2',
                'ip': '172.16.0.2',
                'netmask': '255.255.255.252'
            }
        ],
        'router':
            {
                'protocol': 'ospf',
                'id': '1',
                'routerid': '1.1.1.2',
                'area': '0' 
            }
        }
}
config_device = {}
for device in devices_data.keys():
    config_device[device] = template_int_config.render(devices_data[device]).split('\n')
print(json.dumps(config_device,indent=4))
ip_mgmt = {
    'C8K1': '192.168.1.21',
    'C8K2': '192.168.1.22',
}
for device,configuration in config_device.items():
    host = {
        'device_type': 'cisco_ios',
        'ip': ip_mgmt[device],
        'username': 'cisco',
        'password': 'cisco'
    }
    with ConnectHandler(**host) as connection:
        print(connection.find_prompt())
        print(connection.send_command('show ip int brief'))
        connection.send_config_set(configuration)
        print()
        print(connection.send_command('show ip int brief'))
        print()
        if device == 'C8K2':
            while True:
                ospf_nei = connection.send_command('show ip ospf nei')
                time.sleep(1)
                if len(ospf_nei) > 0:
                    break
            print('Confirmación de vecindad OSPF:')
            print()
            print(connection.find_prompt())
            print(connection.send_command('show ip ospf nei'))
            print()
            print(connection.send_command('show ip route'))