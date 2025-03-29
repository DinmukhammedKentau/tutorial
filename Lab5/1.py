import re
def getDataFromTXT():
    with open("input.txt","r",encoding="utf-8") as file:
        return print(file.read())
#re.search()#КЕЗ КЕЛГЕН ЖЕРДЕН ИЗДЕЙДИ
# re.search() тек ен биринши совподениены гана табады
#re.match() #Тек бас жагынан издейди
#re.findall() # барлык совпадение издейди
#re.sub() #ауыстырат