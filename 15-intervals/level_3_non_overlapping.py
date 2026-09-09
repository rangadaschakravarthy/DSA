"""
Level 3: Non-Overlapping Intervals & Sorting by End Time

Topics Covered:
1. Non-overlapping Intervals (Minimum removals to make non-overlapping O(N log N))

Greedy Strategy:
Sort intervals by END TIME!
To minimize removals, greedily pick the interval that finishes earliest to leave maximum room for future intervals.
"""

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """
    Finds the minimum number of intervals to remove to make the rest non-overlapping.
    """
    if not intervals:
        return 0
        
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    
    removals = 0
    prev_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start < prev_end:
            # Overlap detected! Remove current interval (which ends later or equal)
            removals += 1
        else:
            prev_end = end
            
    return removals


if __name__ == "__main__":
    # Test Non-Overlapping Intervals
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1  # Remove [1, 3]
    assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
    
    print("[SUCCESS] All Level 3 Non-Overlapping Intervals tests passed!")
