from itertools import permutations


def getPermutation(str):
    permutationList = permutations(str)
    for p in permutationList:
        print(''.join(p))


str = input("Write word")
getPermutation(str)
