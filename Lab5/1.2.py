import re
with open("input.txt","r",encoding="utf-8") as file:
 for i in range(len(file.readlines())):
     if re.search(r"ab*",file.readline()):
         print("FOUND!")
     else :
         print("NOT FOUND!")
"""encoding="utf-8" — файлдағы қазақша, орысша символдарды дұрыс оқу үшін."""