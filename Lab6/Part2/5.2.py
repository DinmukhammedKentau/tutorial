booleans=(True,True,True,True)
count=0
"""tuple озгермейтин деректер курылымы"""
result = sum(1 for i in booleans if i )
if result==len(booleans):
    print("True")
else :
    print("False")
    """for i in booleans:
         if i==True:
         c+=1"""