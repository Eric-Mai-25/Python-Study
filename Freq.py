def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example
print(char_frequency("hello"))  
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}