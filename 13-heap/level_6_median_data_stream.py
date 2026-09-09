"""
Level 6: Find Median from Data Stream

Problem:
The median is the middle value in an ordered integer list. 
Design a data structure that supports adding numbers and finding the median of current stream.

Time Complexity: O(log N) per addNum, O(1) findMedian
Space Complexity: O(N) storage
"""
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated) stores lower half
        self.large = []  # min-heap stores upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        # Ensure max of small <= min of large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    print("[PASS] Level 6 Find Median from Data Stream tests passed!")
