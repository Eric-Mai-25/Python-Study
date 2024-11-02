def sum_of_two_numbers(nums, target):
    # Create a dictionary to store numbers and their indices
    indices = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement that would add up to the target
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in indices:
            return [indices[complement], i]
        
        # Otherwise, add the current number and its index to the dictionary
        indices[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(sum_of_two_numbers(nums, target))  # Output: [0, 1]


def contains_duplicate(nums):
    seen = set()  # Create a set to store seen numbers
    
    for num in nums:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)  # Add the number to the set if it's not a duplicate
    
    return False  # No duplicates found

# Example usage:
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
print(contains_duplicate(nums1))  # Output: True
print(contains_duplicate(nums2))  # Output: False