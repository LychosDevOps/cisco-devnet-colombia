<?xml version="1.0" encoding="utf-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="exslt"><sch:ns uri="http://exslt.org/dynamic" prefix="dyn"/><sch:ns uri="http://www.devnet.com/router" prefix="router"/><sch:ns uri="urn:ietf:params:xml:ns:netconf:base:1.0" prefix="nc"/><sch:let name="root" value="/nc:data"/><sch:pattern id="router_choice"><sch:rule context="/nc:data/router:interface"><sch:report test="preceding-sibling::router:interface[router:name=current()/router:name]">Duplicate key "router:name"</sch:report><sch:report test="preceding-sibling::router:interface[router:ip_address=current()/router:ip_address and router:netmask=current()/router:netmask]">Violated uniqueness for "router:ip_address router:netmask"</sch:report></sch:rule><sch:rule context="/nc:data/router:acl"><sch:report test="preceding-sibling::router:acl[router:acl_number=current()/router:acl_number]">Duplicate key "router:acl_number"</sch:report><sch:report test="not(router:acl_number&gt;=1 and router:acl_number&lt;=99) and (router:std_type[not(processing-instruction('dsrl'))] or false())">Found nodes that are valid only when "router:acl_number&gt;=1 and router:acl_number&lt;=99"</sch:report><sch:report test="not(router:acl_number&gt;=100 and router:acl_number&lt;=199) and (router:ext_type[not(processing-instruction('dsrl'))] or false())">Found nodes that are valid only when "router:acl_number&gt;=100 and router:acl_number&lt;=199"</sch:report></sch:rule><sch:rule context="/nc:data/router:acl/router:std_type"><sch:report test="preceding-sibling::router:std_type[router:index=current()/router:index]">Duplicate key "router:index"</sch:report><sch:report test="preceding-sibling::router:std_type[router:address=current()/router:address and router:wildcard=current()/router:wildcard]">Violated uniqueness for "router:address router:wildcard"</sch:report></sch:rule><sch:rule context="/nc:data/router:acl/router:ext_type"><sch:report test="preceding-sibling::router:ext_type[router:index=current()/router:index]">Duplicate key "router:index"</sch:report><sch:report test="preceding-sibling::router:ext_type[router:src_address=current()/router:src_address and router:src_wildcard=current()/router:src_wildcard and router:dst_address=current()/router:dst_address and router:dst_wildcard=current()/router:dst_wildcard and router:port=current()/router:port]">Violated uniqueness for "router:src_address router:src_wildcard router:dst_address router:dst_wildcard router:port"</sch:report></sch:rule><sch:rule context="/nc:data/router:router/router:router_type"><sch:report test="preceding-sibling::router:router_type[router:router=current()/router:router]">Duplicate key "router:router"</sch:report></sch:rule><sch:rule context="/nc:data/router:router/router:router_type/router:interfaces"><sch:report test=". = preceding-sibling::router:interfaces">Duplicate leaf-list entry "<sch:value-of select="."/>".</sch:report><sch:report test="not(../../../router:interface/router:name=.)">Leaf "../../../router:interface/router:name" does not exist for leafref value "<sch:value-of select="."/>"</sch:report></sch:rule></sch:pattern></sch:schema>
