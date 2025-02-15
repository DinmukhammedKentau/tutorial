n,k,l = 5,1,3
sum=0
counter =0
array = [0]*n
for i in range(n):
    array[i]=int(input())
for i in range(n):
    if i>=k and i<=3:
        sum+=array[i]
        counter+=1
print(round(sum/counter))