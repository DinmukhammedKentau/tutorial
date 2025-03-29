import os

p1 = os.access(".", os.F_OK)  # Барма жокпа соны тексереди Exist
# Ал F деген ол File деген создин кыскартылган  тури
#access деген доступ деген магына
path = "."
isExist = os.access(path, os.F_OK)
if not isExist:
    print("Current directory doesn't exist")
else:
    print(isExist)
    print("Readable", os.access(path, os.R_OK))
    print("Writable", os.access(path, os.W_OK))
    print("Executable", os.access(path, os.X_OK))
