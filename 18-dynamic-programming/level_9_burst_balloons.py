"""
Level 9: Burst Balloons (Interval DP)

Problem:
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If you burst balloon i, you get nums[i - 1] * nums[i] * nums[i + 1] coins.
Return the maximum coins you can collect by bursting the balloons wisely.

Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""

def max_coins(nums: list[int]) -> int:
    arr = [1] + [x for x in nums if x > 0] + [1]
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n - 1):
        for left in range(0, n - length - 1):
            right = left + length + 1
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    arr[left] * arr[k] * arr[right] + dp[left][k] + dp[k][right]
                )

    return dp[0][n - 1]


if __name__ == "__main__":
    assert max_coins([3, 1, 5, 8]) == 167
    assert max_coins([1, 5]) == 10
    print("[PASS] Level 9 Burst Balloons tests passed!")
