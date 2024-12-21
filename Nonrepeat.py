def first_non_repeating_char(s: str) -> str:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Example
print(first_non_repeating_char("swiss"))  # "w"
print(first_non_repeating_char("aabbcc"))  # None