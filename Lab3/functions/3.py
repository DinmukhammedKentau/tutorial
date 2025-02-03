def solve(numheads,numlegs):
    y=(numlegs-2*numheads)//2
    x=numheads-y
    return y,x
numheads=35
numlegs=94
qoyan,tauyq=solve(numheads,numlegs)
print(qoyan)
print(tauyq)