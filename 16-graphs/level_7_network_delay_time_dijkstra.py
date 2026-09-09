"""
Level 7: Network Delay Time (Dijkstra's Shortest Path Algorithm)

Problem:
You are given a network of n nodes, labeled 1 to n. 
You are given times, a list of travel times as directed edges times[i] = (ui, vi, wi).
We send a signal from a given node k. Return the minimum time it takes for all n nodes to receive the signal.

Time Complexity: O(E log V)
Space Complexity: O(V + E)
"""
from collections import defaultdict
import heapq

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
        
    min_heap = [(0, k)]  # (dist, node)
    distances = {}
    
    while min_heap:
        time, node = heapq.heappop(min_heap)
        
        if node in distances:
            continue
        distances[node] = time
        
        for neighbor, weight in graph[node]:
            if neighbor not in distances:
                heapq.heappush(min_heap, (time + weight, neighbor))
                
    return max(distances.values()) if len(distances) == n else -1


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    assert network_delay_time(times, 4, 2) == 2
    assert network_delay_time([[1, 2, 1]], 2, 1) == 1
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1
    print("[PASS] Level 7 Network Delay Time (Dijkstra) tests passed!")
