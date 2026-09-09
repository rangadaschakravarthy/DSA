"""
Level 5: Non-overlapping Intervals

Problem:
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Time Complexity: O(N log N)
Space Complexity: O(1)
"""

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
        
    intervals.sort(key=lambda x: x[1])
    removals = 0
    prev_end = float('-inf')
    
    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            removals += 1
            
    return removals


if __name__ == "__main__":
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
    print("[PASS] Level 5 Non-overlapping Intervals tests passed!")
