def kv(a,b):
    for i in range(a,b+1):
        yield i**22
a=int(input("Enter a:"))
b=int(input("Enter b:"))
for i in kv(a,b):
    print(i)