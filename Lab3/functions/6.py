def abc(arr):
    arr.reverse()
    return ''.join(arr)
arr=list(input())
print(abc(arr))