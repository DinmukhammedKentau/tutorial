import json
def connection():
    str='''Interface Status
================================================================================
DN                                                 Description           Speed    MTU'''
    print(str)
    with open("sample-data.json","r") as file:
        fromFile=json.load(file)
        array=fromFile["imdata"]
        for i in array:
            tn=i["l1PhysIf"]["attributes"]["dn"]
            description=i["l1PhysIf"]["attributes"]["descr"]
            speed=i["l1PhysIf"]["attributes"]["speed"]
            mtu=i["l1PhysIf"]["attributes"]["mtu"]
            print(f"{tn}                   {description}            {speed}      {mtu}")
        file.close()
connection()