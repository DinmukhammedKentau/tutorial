def getUniqueElements(listOfNumbers):
    uniqueNumbers = set()
    for n in listOfNumbers:
        uniqueNumbers.add(n)
    print(uniqueNumbers)
numbers=list(map(int,input().split()))
getUniqueElements(numbers)