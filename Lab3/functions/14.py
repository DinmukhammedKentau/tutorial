# utils.py

import random
import math

# Function for histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

# Function to check if a word is palindrome
def is_palindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]

# Function to get the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Function to check if a list has adjacent 3's
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Function to check if the list contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# Function to return unique elements in a list
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
