"""
Level 2: House Robber I & II

Problem:
1. House Robber I: Determine maximum money you can rob tonight without alerting police (cannot rob adjacent houses).
2. House Robber II: All houses are arranged in a circle.

Time Complexity: O(N)
Space Complexity: O(1)
"""

def rob_linear(nums: list[int]) -> int:
    prev2, prev1 = 0, 0
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2, prev1 = prev1, curr
    return prev1


def rob_circular(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    assert rob_linear([1, 2, 3, 1]) == 4
    assert rob_linear([2, 7, 9, 3, 1]) == 12
    assert rob_circular([2, 3, 2]) == 3
    assert rob_circular([1, 2, 3, 1]) == 4
    print("[PASS] Level 2 House Robber I & II tests passed!")
