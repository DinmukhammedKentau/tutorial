numbers=list(map(int,input("Number engiz").split()))
isPrime = lambda n:n>1 and all(n%i!=0 for i in range(2,n))
prime_numbers = list (filter(isPrime,numbers))
print(prime_numbers)