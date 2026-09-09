"""
Level 5: Time-Window Call Counter Queue

Topics Covered:
1. Number of Recent Calls within 3000ms O(1) amortized

Complexity:
- Time Complexity: O(1) amortized per ping.
- Space Complexity: O(W) where W is number of requests in 3000ms window.
"""

from collections import deque

class RecentCounter:
    """Counts number of recent requests within time frame [t - 3000, t]."""
    
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


if __name__ == "__main__":
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3  # Ping at 1 popped
    
    print("[SUCCESS] All Level 5 Recent Calls Queue tests passed!")
