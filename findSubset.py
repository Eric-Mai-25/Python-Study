def find_subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result

# Example
print(find_subsets([1, 2, 3]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]