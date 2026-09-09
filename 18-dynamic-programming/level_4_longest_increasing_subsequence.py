"""
Level 4: Longest Increasing Subsequence (LIS)

Problem:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Time Complexity: O(N log N) using binary search / bisect
Space Complexity: O(N) tail array storage
"""
import bisect

def length_of_lis(nums: list[int]) -> int:
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)


if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4  # [2, 3, 7, 101]
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1
    print("[PASS] Level 4 Longest Increasing Subsequence tests passed!")
