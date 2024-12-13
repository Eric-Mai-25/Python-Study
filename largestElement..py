def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)

# Example
print(find_largest([3, 1, 4, 1, 5, 9]))  # Output: 9