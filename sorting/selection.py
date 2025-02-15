import random
arr=[]
for i in range(10):
    arr.append(random.randint(0,10))
for i in range(10):
    min_index=i
    for j in range(i+1,10):
        if arr[min_index] > arr[j]:
            min_index=j
    arr[min_index], arr[i] = arr[i], arr[min_index]
print(arr)