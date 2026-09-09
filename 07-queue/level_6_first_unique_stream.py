"""
Level 6: First Unique Stream Queue & Frequency Map

Topics Covered:
1. First Unique Number in a Stream O(1) amortized

Logic:
Maintain a Queue of numbers and a Hash Map of frequency counts.
When `showFirstUnique()` is called, pop non-unique elements from front of queue.
"""

from collections import deque, Counter

class FirstUnique:
    def __init__(self, nums: list[int]):
        self.counts = Counter(nums)
        self.queue = deque(nums)

    def showFirstUnique(self) -> int:
        while self.queue and self.counts[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        self.counts[value] += 1
        self.queue.append(value)


if __name__ == "__main__":
    fu = FirstUnique([2, 3, 5])
    assert fu.showFirstUnique() == 2
    fu.add(2)
    assert fu.showFirstUnique() == 3
    fu.add(3)
    assert fu.showFirstUnique() == 5
    fu.add(5)
    assert fu.showFirstUnique() == -1
    
    print("[SUCCESS] All Level 6 First Unique Stream tests passed!")
