"""
Level 7: Expert Array Interval Merging & Sweep-Line

Topics Covered:
1. Merge Overlapping Array Ranges O(N log N)
2. Meeting Rooms II (Min Meeting Rooms required using Sweep-Line / Priority Queue O(N log N))

Complexity:
- Time Complexity: O(N log N) for sorting start/end times.
- Space Complexity: O(N) auxiliary space.
"""

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """
    Finds minimum number of conference rooms required for meetings.
    Uses Sweep-Line / Two-Pointer Sorting on Start and End times.
    """
    if not intervals:
        return 0
        
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    start_ptr, end_ptr = 0, 0
    rooms = 0
    max_rooms = 0
    
    while start_ptr < len(intervals):
        if starts[start_ptr] < ends[end_ptr]:
            rooms += 1
            start_ptr += 1
        else:
            rooms -= 1
            end_ptr += 1
        max_rooms = max(max_rooms, rooms)
        
    return max_rooms


if __name__ == "__main__":
    # Test Meeting Rooms II
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    
    print("[SUCCESS] All Level 7 Array Expert tests passed!")
