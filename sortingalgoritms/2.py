n=int(input())
array=[]
barray=[]
for i in range(n):
    k=int(input())
    array.append(k)
for i in range(n):
    if i%2==0:
        barray.append(array[i])
print(min(array))
