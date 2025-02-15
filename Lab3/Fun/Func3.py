def solve(numheads,numlegs):
    rabbit=(numlegs-2*numheads)/2
    chicken=numheads-rabbit
    print(f"{int(rabbit)}, {int(chicken)}")
numheads=35
numlegs=94
solve(numheads,numlegs)
