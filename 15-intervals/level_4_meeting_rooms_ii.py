"""
Level 4: Meeting Rooms II (Minimum Conference Rooms Required)

Problem:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Time Complexity: O(N log N)
Space Complexity: O(N) min-heap size
"""
import heapq

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
        
    intervals.sort(key=lambda x: x[0])
    free_rooms = []  # Min-heap storing end times
    
    heapq.heappush(free_rooms, intervals[0][1])
    
    for i in range(1, len(intervals)):
        # If room with earliest end time is free, reuse it
        if free_rooms[0] <= intervals[i][0]:
            heapq.heappop(free_rooms)
            
        heapq.heappush(free_rooms, intervals[i][1])
        
    return len(free_rooms)


if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    print("[PASS] Level 4 Meeting Rooms II tests passed!")
