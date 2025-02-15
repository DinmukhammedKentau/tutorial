def three(has3):
    for i in range(len(has3)-1):
        if has3[i]==has3[i+1] and has3[i]==3:
            return True
    return False

arr=list(map(int,input().split()))
print(three(arr))
