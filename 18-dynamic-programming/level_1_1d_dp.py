"""
Level 1: 1D Dynamic Programming Foundations

Topics Covered:
1. House Robber O(N) time, O(1) space
2. Coin Change (Fewest coins to make up amount) O(N * Amount)

1D DP Transitions:
- House Robber: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
- Coin Change: dp[i] = min(dp[i], dp[i - coin] + 1)
"""

def house_robber(nums: list[int]) -> int:
    """
    Finds maximum money you can rob without alerting police (cannot rob adjacent houses).
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
        
    prev2, prev1 = 0, 0
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr
        
    return prev1


def coin_change(coins: list[int], amount: int) -> int:
    """
    Finds fewest number of coins needed to make up amount.
    Returns -1 if impossible.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    # Test House Robber
    assert house_robber([1, 2, 3, 1]) == 4  # Rob house 1 ($1) + house 3 ($3) = $4
    assert house_robber([2, 7, 9, 3, 1]) == 12
    
    # Test Coin Change
    assert coin_change([1, 2, 5], 11) == 3  # 11 = 5 + 5 + 1
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    
    print("[SUCCESS] All Level 1 1D DP tests passed!")
