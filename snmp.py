from pysnmp.entity.rfc3413.oneliner import cmdgen
cmdGen = cmdgen.CommandGenerator()
cisco_contact_info_oid = "1.3.6.1.4.1.9.2.1.61.0"
system_up_time_oid = "1.3.6.1.2.1.1.3.0"
hostname = "1.3.6.1.2.1.1.5.0"
input = "1.3.6.1.4.1.2636.3.3.1.1.4.561"
output = "1.3.6.1.4.1.2636.3.3.1.1.1.578"
serial = "1.3.6.1.4.1.2636.3.1.3.0"


errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(cmdgen.CommunityData('allyours'), 
cmdgen.UdpTransportTarget(('10.29.91.1', 161)),
cisco_contact_info_oid,
system_up_time_oid,
hostname,
input,
output,
serial

)

for name, val in varBinds:
    #print('%s = %s' % (name.prettyPrint(), str(val)))
    print('%s = %s' % (name.prettyPrint(), str(val)))
