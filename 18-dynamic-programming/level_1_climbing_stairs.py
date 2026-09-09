"""
Level 1: Climbing Stairs & Min Cost Climbing Stairs

Problem:
1. Climbing Stairs: You are climbing a staircase. It takes n steps to reach the top. 
   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to top?
2. Min Cost Climbing Stairs: Pay cost[i] to step from i. Find min cost to reach top.

Time Complexity: O(N)
Space Complexity: O(1) space optimization
"""

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)
    prev2, prev1 = 0, 0
    for i in range(2, n + 1):
        curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2, prev1 = prev1, curr
    return prev1


if __name__ == "__main__":
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    print("[PASS] Level 1 Climbing Stairs tests passed!")
