array= []
n=int(input())
for i in range(n):
    array.append(int(input("san engiz\n")))

index=0
index2=0
max=array[0]
min=array[0]
for i in range(1,n):
        if array[i]>max:
            max=array[i]
            index=i
        if array[i]<min:
            min=array[i]
            index2=i
a=array[index]
array[index]=array[index2]
array[index2]=a
print(array)
