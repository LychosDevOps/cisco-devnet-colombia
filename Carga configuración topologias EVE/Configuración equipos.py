from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, Environment
import yaml
import json

############ Crear Plantilla #############

with open('data/link_devices.yml') as link_devices_data:
    link_devices_yaml = link_devices_data.read()
link_devices = yaml.safe_load(link_devices_yaml)
# print(json.dumps(link_devices['CRS02ARA'],indent=4))
template_dir = FileSystemLoader('templates')
template_env = Environment(loader=template_dir)
host_configuration = {}

for host,data in link_devices.items():
    if 'RTH' in host:
        template_config = template_env.get_template('devices_templates_huawei.j2')
    elif 'RR'in host:
        template_config = template_env.get_template('devices_templates_cisco_ios.j2')
    else:
        template_config = template_env.get_template('devices_templates_cisco_xr.j2')
    host_configuration[host] = template_config.render(data).split('\n')

######### Conexión equipo ###############

with open('data/devices_connection_data.yml') as devices_connection_data:
    devices_connection_yaml = devices_connection_data.read()
devices_connection = yaml.safe_load(devices_connection_yaml)

for device_conection in devices_connection:
    host = {
        'device_type': device_conection['device_type'],
        'host': device_conection['ip_mgmt'],
        'username': device_conection['username'],
        'password': device_conection['password']
    }
    with ConnectHandler(**host) as connection:
        ######## Configuración según plantilla de equipo ##########
        print ('Iniciando configuración en {host}'.format(host=device_conection['hostname']))
        if "RTH" in device_conection['hostname']:
            connection.send_config_set(host_configuration[device_conection['hostname']],exit_config_mode=False)
        else:
            connection.send_config_set(host_configuration[device_conection['hostname']])
        if 'RR' in device_conection['hostname']:
            connection.save_config()
        elif 'RTH' in device_conection['hostname']:
            print('Equipo {} configurado.'.format(device_conection['hostname']))            
            continue
        else:
            connection.commit()
        # if device_conection['hostname'] in connection.find_prompt():
        print('Equipo {} configurado.'.format(device_conection['hostname']))