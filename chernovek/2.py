def kaitar(a):
    for i in range(a,-1,-1):
        yield i
a=int(input("Enter a:"))
print(list(kaitar(a)))