def find_peak(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return nums[left]

# Example
print(find_peak([1, 2, 3, 1]))  # 3
print(find_peak([1, 2, 1, 3, 5, 6, 4]))  # 6