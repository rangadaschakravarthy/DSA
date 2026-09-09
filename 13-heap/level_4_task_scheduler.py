"""
Level 4: Task Scheduler

Problem:
Given a characters array tasks representing tasks CPU needs to do, and an integer n representing cooldown between same tasks,
return the minimum number of units of time required to complete all tasks.

Time Complexity: O(N)
Space Complexity: O(1) fixed frequency array
"""
from collections import Counter
import heapq

def least_interval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_freq = max(counts.values())
    max_count = sum(1 for count in counts.values() if count == max_freq)
    
    time = (max_freq - 1) * (n + 1) + max_count
    return max(len(tasks), time)


if __name__ == "__main__":
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert least_interval(["A", "C", "A", "B", "D", "B"], 1) == 6
    print("[PASS] Level 4 Task Scheduler tests passed!")
