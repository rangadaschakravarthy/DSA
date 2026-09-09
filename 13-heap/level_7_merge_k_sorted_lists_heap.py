"""
Level 7: Merge K Sorted Lists / Arrays using Heap

Problem:
You are given an array of k sorted arrays/lists, merge all the sorted lists into one sorted list using Heap.

Time Complexity: O(N log K)
Space Complexity: O(K) min-heap size
"""
import heapq

def merge_k_sorted_arrays(arrays: list[list[int]]) -> list[int]:
    min_heap = []
    # Push (val, array_idx, element_idx)
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    result = []
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))

    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    assert merge_k_sorted_arrays(lists) == [1, 1, 2, 3, 4, 4, 5, 6]
    print("[PASS] Level 7 Merge K Sorted Arrays tests passed!")
