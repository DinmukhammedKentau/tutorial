import random
array=[]
for i in range(20):
    array.append(random.randint(1,15))
for i in range(20):
    for j in range(0,20-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)