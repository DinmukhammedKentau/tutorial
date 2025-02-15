def nolnolsem(arr):
    barr=[]
    for i in arr:
        if i==0 or i==7:
            barr.append(i)
    if barr[0]==0 and barr[1]==0 and barr[2]==7 and len(barr)==3:
        return True
    return False


print(nolnolsem([1,2,4,0,0,7,5]))
print(nolnolsem([1,0,2,4,0,5,7]))
print(nolnolsem([1,7,2,0,4,5,0]))
print()

while True:
       arr = list(map(int, input().split()))
       print(nolnolsem(arr))
       if arr==[0]:
           break
