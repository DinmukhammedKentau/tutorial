import itertools

def print_permutations():
    user_input = input("Engiz ")
    permutations = itertools.permutations(user_input)
    for perm in permutations:
        result = ''
        for char in perm:
            result += char
        print(result)


print_permutations()
