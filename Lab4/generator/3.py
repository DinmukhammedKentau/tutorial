def getDiv12(a):
    for i in range(n+1):
        if i % 12 == 0:
            yield i
n=int(input("Enter N:"))
for i in getDiv12(n):
    print(i)