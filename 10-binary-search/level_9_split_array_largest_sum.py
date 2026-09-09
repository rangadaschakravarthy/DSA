"""
Level 9: Split Array Largest Sum

Problem:
Given an integer array nums and an integer k, split nums into k non-empty subarrays 
such that the largest sum of any subarray is minimized. Return the minimized largest sum.

Time Complexity: O(N * log(sum(nums)))
Space Complexity: O(1)
"""

def split_array(nums: list[int], k: int) -> int:
    def can_split(max_allowed_sum):
        count = 1
        curr_sum = 0
        for num in nums:
            if curr_sum + num > max_allowed_sum:
                count += 1
                curr_sum = num
            else:
                curr_sum += num
        return count <= k

    left, right = max(nums), sum(nums)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if can_split(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


if __name__ == "__main__":
    assert split_array([7, 2, 5, 10, 8], 2) == 18
    assert split_array([1, 2, 3, 4, 5], 2) == 9
    print("[PASS] Level 9 Split Array Largest Sum tests passed!")
