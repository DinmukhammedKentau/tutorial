import os

path="."
isExist=os.access(path,os.F_OK)
if not isExist:
    print("File not found")
else :
    list = ["avadakedavra","expect to patronum","expilliarmus"]
    with open("file.txt","w")as file:
        for i in list:
            file.write(i+"\n")



