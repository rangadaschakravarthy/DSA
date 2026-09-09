"""
Level 4: Weighted Shortest Path & Dijkstra's Algorithm

Topics Covered:
1. Dijkstra's Algorithm O((V + E) log V) with Min-Heap
2. Network Delay Time (Max Shortest Path to All Nodes)

Complexity:
- Time Complexity: O((V + E) log V) using priority queue (`heapq`).
- Space Complexity: O(V + E) for adjacency list and distance map.
"""

import heapq
from collections import defaultdict

def dijkstra(n: int, edges: list[list[int]], start: int) -> dict[int, int]:
    """
    Computes shortest path distances from start node to all reachable nodes in a weighted graph.
    edges format: [u, v, weight]
    """
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[start] = 0
    
    # Priority Queue storing tuples: (current_distance, node)
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > distances[u]:
            continue
            
        for v, weight in adj[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))
                
    return distances


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    """
    Finds the minimum time for all n nodes to receive a signal sent from node k.
    Returns -1 if not all nodes can receive the signal.
    """
    distances = dijkstra(n, times, k)
    max_time = max(distances.values())
    return max_time if max_time != float('inf') else -1


if __name__ == "__main__":
    # Test Dijkstra & Network Delay Time
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    assert network_delay_time(times1, 4, 2) == 2  # Signal reaches 1 at t=1, 3 at t=1, 4 at t=2
    
    times2 = [[1, 2, 1]]
    assert network_delay_time(times2, 2, 1) == 1
    assert network_delay_time(times2, 2, 2) == -1
    
    print("[SUCCESS] All Level 4 Dijkstra Algorithm tests passed!")
