import json
str='''Interface Status
================================================================================
DN                                                 Description           Speed    MTU'''
print(str)
with open("sample-data.json","r")as file:
    data=json.load(file)
    array=data["imdata"]
    for i in array:
        tn=i["l1PhysIf"]["attributes"]
        print(f"{tn["dn"]} {tn["descr"]} {tn['speed']} {tn['mtu']}")


