def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(nums)

# Example
print(find_missing_number([1, 2, 4, 5, 6]))  # Output: 3