def spy_game(nums):
    code = [0, 0, 7]  # Sequence to find
    for num in nums:
        if num == code[0]:  # Check if current number matches first in sequence
            code.pop(0)  # Remove matched number
        if not code:  # If all elements are matched
            return True
    return False

# Example usage:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
