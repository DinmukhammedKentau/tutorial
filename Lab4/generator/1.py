import math
def getSquares():
    a=0
    while True:
      yield pow(a,2)


n=int(input("Enter N:"))
for i in range(n):
    print(next(getSquares()))