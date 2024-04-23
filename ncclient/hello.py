from ncclient import manager

show_int_G1 = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
</filter>
'''

namespace = {"native": "http://cisco.com/ns/yang/Cisco-IOS-XE-native"}
xpath = "/native/interface/GigabitEthernet[name='1']/ip/address/primary/netmask"

with manager.connect(host="192.168.1.21", 
                     port=830, 
                     username="cisco",
                     password="cisco", 
                     hostkey_verify=False, 
                     device_params = {'name':'iosxe'}) as m:
    # for capability in m.server_capabilities:
        # print(capability)
    show_interfaces = m.get(filter=('xpath',(namespace,xpath)))
    print(show_interfaces)
 
    # c = m.get_config(source='running').data_xml
    # with open("%s.xml" % host, 'w') as f:
    #     f.write(c)