def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore case and spaces
    return s == s[::-1]

# Example
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("A man a plan a canal Panama"))  # Output: True