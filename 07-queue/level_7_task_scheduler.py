"""
Level 7: Task Scheduler Queue & Priority Queue Cooling

Topics Covered:
1. Task Scheduler CPU Idle Time Calculation O(N)

Logic:
1. Count task frequencies and maintain Max-Heap of frequencies.
2. Use Queue to store cooled tasks: `(cnt, available_time)`.
3. Process tasks unit time by unit time.
"""

import heapq
from collections import Counter, deque

def least_interval(tasks: list[str], n: int) -> int:
    """
    Finds minimum CPU intervals needed to execute all tasks with cooling period n.
    """
    counts = Counter(tasks)
    max_heap = [-cnt for cnt in counts.values()]
    heapq.heapify(max_heap)
    
    # Cooling queue stores tuples: (rem_count, available_time)
    q = deque()
    time = 0
    
    while max_heap or q:
        time += 1
        
        if max_heap:
            cnt = heapq.heappop(max_heap) + 1  # Process task (decrement remaining)
            if cnt < 0:
                q.append((cnt, time + n))
                
        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
            
    return time


if __name__ == "__main__":
    assert least_interval(["A","A","A","B","B","B"], 2) == 8  # A -> B -> idle -> A -> B -> idle -> A -> B
    assert least_interval(["A","A","A","B","B","B"], 0) == 6
    
    print("[SUCCESS] All Level 7 Task Scheduler tests passed!")
