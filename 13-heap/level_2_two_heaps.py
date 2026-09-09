"""
Level 2: Two Heaps Pattern for Streaming Data

Topics Covered:
1. Find Median from Data Stream (Max-Heap + Min-Heap O(log N) insert, O(1) median)

Two-Heap Invariants:
1. `max_heap` stores lower half of numbers (inverted values for max-heap).
2. `min_heap` stores upper half of numbers.
3. Size invariant: len(max_heap) == len(min_heap) OR len(max_heap) == len(min_heap) + 1.
4. Value invariant: max(max_heap) <= min(min_heap).
"""

import heapq

class MedianFinder:
    """
    Data structure that supports adding numbers from a data stream and finding median in O(1) time.
    """
    
    def __init__(self):
        # max_heap stores lower half (invert signs since heapq is min-heap)
        self.max_heap = []
        # min_heap stores upper half
        self.min_heap = []

    def add_num(self, num: int) -> None:
        # Step 1: Push to max_heap
        heapq.heappush(self.max_heap, -num)
        
        # Step 2: Balance value invariant (max of max_heap <= min of min_heap)
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
            
        # Step 3: Balance size invariant (len(max_heap) >= len(min_heap))
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0


if __name__ == "__main__":
    # Test Streaming Median Finder
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0
    
    print("[SUCCESS] All Level 2 Two-Heaps Median tests passed!")
