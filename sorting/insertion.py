import random
array=[]
for i in range(10):
    array.append(random.randint(0,10))
for i in range(10):
    key=array[i]
    j=i-1
    while j>=0 and key<array[j]:
        array[j+1]=array[j]
        j-=1
    array[j+1]=key
print(array)