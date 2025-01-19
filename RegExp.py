def is_match(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True  # Empty string matches empty pattern

    for j in range(1, len(p) + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]  # '*' can eliminate the preceding element

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                dp[i][j] = dp[i - 1][j - 1]  # Characters match
            elif p[j - 1] == "*":
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == "."))

    return dp[-1][-1]

# Example
print(is_match("aa", "a*"))       # True
print(is_match("mississippi", "mis*is*p*."))  # False
print(is_match("ab", ".*"))      # True