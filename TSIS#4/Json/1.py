import json
'''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
'''

file_path = r"c:\Users\kozha\Desktop\Bored\Python\TSIS#4\Json\sample-data.json"

with open(file_path, "r") as f:
    a = f.read()
data = json.loads(a)
a = b = c = d = ""
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for i in range(len(data["imdata"])):
    a = data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    b = data["imdata"][i]["l1PhysIf"]["attributes"]["descr"]
    c = data["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
    d = data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print("{:<49}{:<23}{:<7}  ".format(a,b,c), d )