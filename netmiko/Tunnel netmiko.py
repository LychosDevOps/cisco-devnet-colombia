import netmiko
import time
from ntc_templates.parse import parse_output
import json
import pandas as pd
import os

pwd = os.environ['pwd']

jumpServer = {
    "device_type": "linux",
    "ip": '127.0.0.1',
    "port": "5101",
    "username": os.environ['USER_MRTG'],
    "password": os.environ['PASS_MRTG']
}


interface_data = {}
with netmiko.ConnectHandler(**jumpServer) as connection:
    # print(connection.find_prompt())
    connection.send_command("ssh "+os.environ['USER_DEVICE_HENDRIX']+"@RTHMEG01 -o StrictHostKeyChecking=no",expect_string="password")
    connection.send_command_timing(os.environ['PASS_DEVICE_HENDRIX'])
    netmiko.redispatch(connection, device_type="huawei")
    out = connection.send_command("display interface description")
    # time.sleep(0.5)
    # print(out)
    # out_IP_0_1_0_0 = connection.send_command("show ip interface brief | include 0/1/0/0", use_textfsm=True)
    output_parsed = parse_output(platform="huawei_vrp", command="display interface description", data=out)
# print(json.dumps(output_parsed,indent=4))
for output_data in output_parsed:
    for output_parsed_keys,output_parsed_value in output_data.items():
        index_Title = output_parsed_keys.upper()
        if index_Title not in interface_data:
            interface_data[index_Title] = [output_parsed_value]
        else:
            interface_data[index_Title].append(output_parsed_value)
# print(interface_data)
data_Pandas = pd.DataFrame(interface_data)
print(data_Pandas[data_Pandas['INTERFACE'] == '50|100GE4/0/0(100G)'])
save_data_path = pwd+"Descripción.xlsx"
data_Pandas.to_excel(save_data_path,sheet_name='RTHMEG01',index=False)