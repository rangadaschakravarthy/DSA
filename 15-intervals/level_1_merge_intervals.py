"""
Level 1: Interval Merging & Sorting by Start Time

Topics Covered:
1. Merge Overlapping Intervals O(N log N)

Algorithm:
1. Sort intervals by start time: interval[0].
2. Iterate through sorted intervals:
   - If merged is empty or current.start > merged[-1].end: append current interval.
   - Else: merge by updating merged[-1].end = max(merged[-1].end, current.end).
"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merges all overlapping intervals.
    """
    if not intervals:
        return []
        
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_start, last_end = merged[-1]
        curr_start, curr_end = current
        
        if curr_start <= last_end:
            merged[-1][1] = max(last_end, curr_end)
        else:
            merged.append(current)
            
    return merged


if __name__ == "__main__":
    # Test Merge Intervals
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    
    print("[SUCCESS] All Level 1 Merge Intervals tests passed!")
