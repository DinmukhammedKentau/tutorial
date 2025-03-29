import os

path = r"C:\Users\Dimash\Desktop\word head english v3.jpg"
isExist = os.access(path, os.F_OK)
if not isExist:
    print("Current directory doesn't exist")
else:
    print(isExist)
    print("Readable", os.access(path, os.R_OK))
    print("Writable", os.access(path, os.W_OK))
    print("Executable", os.access(path, os.X_OK))
    if os.access(path, os.R_OK) and os.access(path, os.W_OK) and os.access(path, os.X_OK):
     os.remove(path)
     """os.rmdir() - бос папканы оширеди"""
     """os.remove() - кез келген файлды ошире алады"""