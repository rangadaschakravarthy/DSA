"""
Level 1: Heap Basics and Operations

Problem:
Implement Min-Heap basic operations: push, pop, peek, and heapify array.

Time Complexity: O(log N) push/pop, O(N) heapify
Space Complexity: O(N) storage
"""
import heapq

def heap_operations(nums: list[int]) -> list[int]:
    # Heapify
    heapq.heapify(nums)
    result = []
    while nums:
        result.append(heapq.heappop(nums))
    return result


if __name__ == "__main__":
    arr = [5, 3, 8, 1, 2]
    sorted_out = heap_operations(arr)
    assert sorted_out == [1, 2, 3, 5, 8]
    print("[PASS] Level 1 Heap Basics tests passed!")
