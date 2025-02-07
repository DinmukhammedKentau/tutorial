def is_palindrome(s):
    # Remove spaces and convert to lowercase for comparison
    s = ''.join(s.split()).lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Example usage:
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
