from itertools import permutations


def print_permutations():
    user_input = input("Enter a string: ")
    perms = [''.join(p) for p in permutations(user_input)]

    print("All permutations:")
    for perm in perms:
        print(perm)


# Call the function
print_permutations()
