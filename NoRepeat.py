def longest_unique_substring(s: str) -> int:
    char_index = {}
    start = max_length = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Example
print(longest_unique_substring("abcabcbb"))  # 3 ("abc")
print(longest_unique_substring("bbbbb"))     # 1 ("b")