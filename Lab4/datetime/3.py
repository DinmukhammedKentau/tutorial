from datetime import datetime
now=str(datetime.now())
print(now)
for i in range(len(now)):
    if i>=20:
        print("0",end="")
    else:
        print(now[i],end="")
