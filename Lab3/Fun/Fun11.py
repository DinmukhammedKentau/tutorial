import string


def checkPalindrome(sozder):
    soz = []
    for i in range(len(sozder)):
        if sozder[i]==' ':
            continue
        if (sozder[i].isalnum()):
            soz.append(sozder[i].lower())
    isExist = True
    for i in range(len(soz)//2):
       if soz[i]!=soz[len(soz)-i-1]:
           isExist=False
           break
    if isExist:
        print("Palindrome")
    else:
        print("Not Palindrome")
soilem=list(map(str,input("Write word: ")))
checkPalindrome(soilem)