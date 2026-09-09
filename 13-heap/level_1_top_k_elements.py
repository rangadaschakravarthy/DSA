"""
Level 1: Top-K Pattern & Min-Heap Optimization

Topics Covered:
1. Kth Largest Element in an Array O(N log K)
2. Top K Frequent Elements O(N log K)

Pattern Insight:
To find K largest elements, maintain a MIN-HEAP of size K!
If heap size exceeds K, pop the smallest element. The remaining elements are the K largest.
"""

import heapq
from collections import Counter

def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Finds the k-th largest element in an unsorted array.
    Uses Min-Heap of size K.
    """
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    return min_heap[0]


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Finds the k most frequent elements in nums.
    """
    counts = Counter(nums)
    min_heap = []
    
    for num, freq in counts.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    return [num for freq, num in min_heap]


if __name__ == "__main__":
    # Test Kth Largest Element
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    
    # Test Top K Frequent
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    
    print("[SUCCESS] All Level 1 Top-K Heap tests passed!")
