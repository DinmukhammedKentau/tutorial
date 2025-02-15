import math
def filterPrime(numbers):
    primes=[]
    for number in numbers:
        isPrime=True
        for i in range(2,int(math.sqrt(number))+1):
            if number % i == 0:
                isPrime=False
                break
        if isPrime:
            primes.append(number)
    return primes
numbers=list(map(int,input().split()))
print(filterPrime(numbers))
