from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    t_count = Counter(t)
    current_count = {}
    required = len(t_count)
    formed = 0
    left, right = 0, 0
    min_length = float('inf')
    min_window_start = 0

    while right < len(s):
        char = s[right]
        current_count[char] = current_count.get(char, 0) + 1
        
        if char in t_count and current_count[char] == t_count[char]:
            formed += 1

        while left <= right and formed == required:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window_start = left
            
            current_count[s[left]] -= 1
            if s[left] in t_count and current_count[s[left]] < t_count[s[left]]:
                formed -= 1
            left += 1

        right += 1

    return "" if min_length == float('inf') else s[min_window_start:min_window_start + min_length]

# Example
print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
print(min_window("a", "a"))               # "a"
print(min_window("a", "aa"))              # ""