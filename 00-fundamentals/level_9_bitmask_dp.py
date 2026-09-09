"""
Level 9: Bitmask Dynamic Programming Foundations (Mastery Level)

Topics Covered:
1. Traveling Salesperson Problem (TSP) using Bitmask State DP O(N^2 * 2^N)

State Definition:
dp[mask][u] = minimum cost to visit all cities in `mask` ending at city `u`.
`mask` is a bitmask of size N where bit i = 1 if city i has been visited.
"""

def tsp_bitmask_dp(dist: list[list[int]]) -> int:
    """
    Solves Traveling Salesperson Problem for N cities (0 to N-1) starting at city 0.
    Returns minimum cost to visit all cities and return to start city 0.
    """
    n = len(dist)
    if n == 0:
        return 0
        
    full_mask = (1 << n) - 1
    # Memoization table: dp[mask][u]
    memo = {}
    
    def solve(mask: int, u: int) -> int:
        if mask == full_mask:
            return dist[u][0]  # Return to start city 0
            
        state = (mask, u)
        if state in memo:
            return memo[state]
            
        min_cost = float('inf')
        for v in range(n):
            if not (mask & (1 << v)):  # City v not visited yet
                cost = dist[u][v] + solve(mask | (1 << v), v)
                min_cost = min(min_cost, cost)
                
        memo[state] = min_cost
        return min_cost
        
    return solve(1, 0)  # Start at city 0 with mask 0b000...1


if __name__ == "__main__":
    # Test TSP Bitmask DP for 4 cities
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    assert tsp_bitmask_dp(dist_matrix) == 80  # 0 -> 1 -> 3 -> 2 -> 0 = 10 + 25 + 30 + 15 = 80
    
    print("[SUCCESS] All Level 9 Bitmask DP Mastery tests passed!")
