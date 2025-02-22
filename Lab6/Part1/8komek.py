import os
import shutil

p1 = os.access(r"C:\Users\Dimash\Рабочий стол\11", os.F_OK)  # Барма жокпа соны тексереди Exist
# Ал F деген ол File деген создин кыскартылган  тури
os.rename(".","8komekke.py")
path = r"C:\Games"

isExist = os.access(path, os.F_OK)
if not isExist:
    print("Current directory doesn't exist")
else:
    print(isExist)
    print("Readable", os.access(path, os.R_OK))
    print("Writable", os.access(path, os.W_OK))
    print("Executable", os.access(path, os.X_OK))
    shutil.rmtree(path)
"""import shutil сосын shutil.rmtree аркылы биз папканы 
жане папканын ишиндеги заттарымен бирге ошируге болады"""