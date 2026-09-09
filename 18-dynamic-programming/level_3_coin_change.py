"""
Level 3: Coin Change & Target Sum

Problem:
1. Coin Change: Return fewest number of coins needed to make up amount. If not possible, return -1.
2. Target Sum: Return number of ways to assign + and - to elements to sum to target.

Time Complexity: O(Amount * N) for Coin Change
Space Complexity: O(Amount)
"""

def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1


def find_target_sum_ways(nums: list[int], target: int) -> int:
    total = sum(nums)
    if (total + target) % 2 != 0 or total < abs(target):
        return 0
    P = (total + target) // 2
    
    dp = [0] * (P + 1)
    dp[0] = 1
    for num in nums:
        for j in range(P, num - 1, -1):
            dp[j] += dp[j - num]
            
    return dp[P]


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5
    print("[PASS] Level 3 Coin Change & Target Sum tests passed!")
