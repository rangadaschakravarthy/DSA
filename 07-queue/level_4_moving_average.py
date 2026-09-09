"""
Level 4: Sliding Window Stream Moving Average

Topics Covered:
1. Moving Average from Data Stream O(1) time per query

Complexity:
- Time Complexity: O(1) per next() call.
- Space Complexity: O(Size) queue size limit.
"""

from collections import deque

class MovingAverage:
    """Calculates moving average of a stream of integers within a sliding window of fixed size."""
    
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)


if __name__ == "__main__":
    ma = MovingAverage(3)
    assert abs(ma.next(1) - 1.0) < 1e-5
    assert abs(ma.next(10) - 5.5) < 1e-5
    assert abs(ma.next(3) - 4.66667) < 1e-4
    assert abs(ma.next(5) - 6.0) < 1e-5
    
    print("[SUCCESS] All Level 4 Moving Average tests passed!")
