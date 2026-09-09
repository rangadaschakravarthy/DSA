"""
Level 8: Employee Free Time

Problem:
We are given a list schedule of employees, which represents the working time for each employee.
Return the list of finite intervals representing common, positive-length free time for all employees, sorted in order.

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

def employee_free_time(schedule: list[list[list[int]]]) -> list[list[int]]:
    # Flatten and sort all working intervals by start time
    intervals = []
    for emp in schedule:
        for interval in emp:
            intervals.append(interval)
            
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for curr in intervals[1:]:
        prev = merged[-1]
        if curr[0] <= prev[1]:
            prev[1] = max(prev[1], curr[1])
        else:
            merged.append(curr)
            
    free_time = []
    for i in range(1, len(merged)):
        free_time.append([merged[i-1][1], merged[i][0]])
        
    return free_time


if __name__ == "__main__":
    sched1 = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    assert employee_free_time(sched1) == [[3, 4]]
    
    sched2 = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
    assert employee_free_time(sched2) == [[5, 6], [7, 9]]
    print("[PASS] Level 8 Employee Free Time tests passed!")
