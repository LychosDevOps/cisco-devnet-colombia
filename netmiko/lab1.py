from netmiko import ConnectHandler
import time
from ntc_templates.parse import parse_output
import json

if __name__ == '__main__': 
    C8K_1 = {
        "device_type" : "cisco_ios",
        "ip": "192.168.3.22",
        "username": "cisco",
        "password": "cisco"
    }

    NXOS = {
        "device_type" : "cisco_nxos",
        "ip": "192.168.3.20",
        "username": "admin",
        "password": "cisco!123"
    }

    try:
        device_IOS = ConnectHandler(**C8K_1)
    except:
        print('No Connection')
    # try:
    #     device_NXOS = ConnectHandler(**NXOS)
    # except ssh_exception.NetmikoAuthenticationException as e:
    #     print(e)
    # except ssh_exception.NetmikoTimeoutException as e:
    #     print(e)

    # print(device.find_prompt())
    show_version_IOS = device_IOS.send_command("show version")
    show_version_parsed_IOS = parse_output(platform="cisco_ios",command="show version",data=show_version_IOS)
    show_version_JSON_IOS = json.dumps(show_version_parsed_IOS, indent=4)
    # show_version_NXOS = device_NXOS.send_command("show version")
    # show_version_parsed_NXOS = parse_output(platform="cisco_nxos",command="show version",data=show_version_NXOS)
    # show_version_JSON_NXOS = json.dumps(show_version_parsed_NXOS, indent=4)
    print(show_version_JSON_IOS)
    with open('outputJSON.txt','w') as data:
        data.write(show_version_JSON_IOS) 
    # print()
    # print(show_version_JSON_NXOS)