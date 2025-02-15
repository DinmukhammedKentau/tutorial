def histogram(numbers):
    for n in numbers:
        for i in range(n):
            print("*",end="")
        print()
numbers=list(map(int,input().split()))
histogram(numbers)