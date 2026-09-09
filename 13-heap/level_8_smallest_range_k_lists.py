"""
Level 8: Smallest Range Covering Elements from K Lists

Problem:
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes 
at least one number from each of the k lists.

Time Complexity: O(N log K) where N total elements
Space Complexity: O(K) heap size
"""
import heapq

def smallest_range(nums: list[list[int]]) -> list[int]:
    min_heap = []
    max_val = float('-inf')

    for i, arr in enumerate(nums):
        heapq.heappush(min_heap, (arr[0], i, 0))
        max_val = max(max_val, arr[0])

    range_start, range_end = -10**9, 10**9

    while len(min_heap) == len(nums):
        min_val, r, c = heapq.heappop(min_heap)

        if max_val - min_val < range_end - range_start:
            range_start, range_end = min_val, max_val

        if c + 1 < len(nums[r]):
            nxt = nums[r][c + 1]
            heapq.heappush(min_heap, (nxt, r, c + 1))
            max_val = max(max_val, nxt)

    return [range_start, range_end]


if __name__ == "__main__":
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    assert smallest_range(nums) == [20, 24]
    print("[PASS] Level 8 Smallest Range Covering Elements from K Lists tests passed!")
