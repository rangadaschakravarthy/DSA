"""
Level 6: Task Scheduler (Greedy Approach)

Problem:
Given a characters array tasks representing tasks CPU needs to do, and an integer n representing cooldown between same tasks,
return the minimum number of units of time required to complete all tasks.

Time Complexity: O(N)
Space Complexity: O(1)
"""
from collections import Counter

def least_interval_greedy(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_freq = max(counts.values())
    max_count = sum(1 for count in counts.values() if count == max_freq)
    
    empty_slots = (max_freq - 1) * (n - (max_count - 1))
    available_tasks = len(tasks) - (max_freq * max_count)
    idles = max(0, empty_slots - available_tasks)
    
    return len(tasks) + idles


if __name__ == "__main__":
    assert least_interval_greedy(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert least_interval_greedy(["A", "C", "A", "B", "D", "B"], 1) == 6
    print("[PASS] Level 6 Greedy Task Scheduler tests passed!")
