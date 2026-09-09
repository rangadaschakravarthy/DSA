"""
Level 6: 0/1 Knapsack & Partition Equal Subset Sum

Problem:
1. 0/1 Knapsack: Given weights and values of N items, find max value that fits in capacity W.
2. Partition Equal Subset Sum: Check if array can be partitioned into two subsets with equal sum.

Time Complexity: O(N * W) / O(N * Target)
Space Complexity: O(W) space optimization
"""

def knapsack_01(weights: list[int], values: list[int], W: int) -> int:
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]


def can_partition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


if __name__ == "__main__":
    assert knapsack_01([1, 2, 3], [10, 15, 40], 6) == 65
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 2, 3, 5]) == False
    print("[PASS] Level 6 0/1 Knapsack tests passed!")
