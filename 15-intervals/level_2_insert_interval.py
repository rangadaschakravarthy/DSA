"""
Level 2: In-Place Interval Insertion

Topics Covered:
1. Insert Interval O(N) single pass

Algorithm (3 Phases):
1. Add all intervals ending BEFORE new_interval starts.
2. Merge all overlapping intervals with new_interval.
3. Add all remaining intervals starting AFTER new_interval ends.
"""

def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    Inserts new_interval into intervals (which is sorted by start time and non-overlapping).
    """
    result = []
    i = 0
    n = len(intervals)
    
    # Phase 1: Add intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
        
    # Phase 2: Merge overlapping intervals with new_interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)
    
    # Phase 3: Add remaining intervals after new_interval
    while i < n:
        result.append(intervals[i])
        i += 1
        
    return result


if __name__ == "__main__":
    # Test Insert Interval
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    
    print("[SUCCESS] All Level 2 Insert Interval tests passed!")
