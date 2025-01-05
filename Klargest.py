import heapq

def kth_largest(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]

# Example
print(kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4