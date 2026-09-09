"""
Level 3: 0/1 Knapsack & Subset Sum Optimization

Topics Covered:
1. 0/1 Knapsack Maximum Value O(N * Capacity) with 1D Space Optimization
2. Partition Equal Subset Sum O(N * Target_Sum)

1D Knapsack Space Optimization:
Traverse capacity loop BACKWARDS (from capacity down to weight) to prevent reusing the same item multiple times!
dp[w] = max(dp[w], dp[w - weight] + value)
"""

def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Solves classic 0/1 Knapsack problem returning max value for given capacity.
    """
    dp = [0] * (capacity + 1)
    
    for weight, val in zip(weights, values):
        # Iterate capacity backwards for 0/1 Knapsack (each item used at most once)
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + val)
            
    return dp[capacity]


def can_partition_subset_sum(nums: list[int]) -> bool:
    """
    Determines if array can be partitioned into two subsets with equal sum.
    Reduces to finding if there exists a subset with sum == total_sum // 2.
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
        
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum 0 is always possible (empty subset)
    
    for num in nums:
        for w in range(target, num - 1, -1):
            if dp[w - num]:
                dp[w] = True
                
    return dp[target]


if __name__ == "__main__":
    # Test 0/1 Knapsack
    weights = [1, 2, 3]
    values = [6, 10, 12]
    assert knapsack_01(weights, values, 5) == 22  # Pick item 2 ($10) + item 3 ($12) = $22
    
    # Test Partition Equal Subset Sum
    assert can_partition_subset_sum([1, 5, 11, 5]) is True   # [1, 5, 5] and [11]
    assert can_partition_subset_sum([1, 2, 3, 5]) is False
    
    print("[SUCCESS] All Level 3 0/1 Knapsack tests passed!")
