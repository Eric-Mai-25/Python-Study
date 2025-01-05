def array_intersection(arr1: list[int], arr2: list[int]) -> list[int]:
    return list(set(arr1) & set(arr2))

# Example
print(array_intersection([1, 2, 2, 3], [2, 2, 4]))  # [2]
print(array_intersection([1, 2, 3], [4, 5, 6]))    # []