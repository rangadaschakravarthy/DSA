"""
Level 8: Cheapest Flights Within K Stops (Bellman-Ford / Modified BFS)

Problem:
There are n cities connected by flights. Given flights[i] = [from, to, price], 
find the cheapest price from src to dst with at most k stops.

Time Complexity: O(K * E)
Space Complexity: O(V)
"""

def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    prices = [float('inf')] * n
    prices[src] = 0
    
    for _ in range(k + 1):
        temp_prices = list(prices)
        for u, v, price in flights:
            if prices[u] != float('inf'):
                temp_prices[v] = min(temp_prices[v], prices[u] + price)
        prices = temp_prices
        
    return prices[dst] if prices[dst] != float('inf') else -1


if __name__ == "__main__":
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert find_cheapest_price(3, flights, 0, 2, 1) == 200
    assert find_cheapest_price(3, flights, 0, 2, 0) == 500
    print("[PASS] Level 8 Cheapest Flights Within K Stops tests passed!")
