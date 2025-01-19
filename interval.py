def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
    merged = [intervals[0]]  # Initialize with the first interval
    
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:  # Overlapping intervals
            previous[1] = max(previous[1], current[1])  # Merge
        else:
            merged.append(current)  # No overlap, add to result
    
    return merged

# Example
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Output: [[1, 6], [8, 10], [15, 18]]