def max_area(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_area([1, 1]))                       # 1