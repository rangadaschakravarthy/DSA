"""
Level 1: Graph BFS and DFS Traversals

Problem:
Implement Breadth-First Search (BFS) and Depth-First Search (DFS) traversals on an adjacency list graph.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""
from collections import deque, defaultdict

def bfs(graph: dict[int, list[int]], start_node: int) -> list[int]:
    visited = set([start_node])
    queue = deque([start_node])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return order


def dfs(graph: dict[int, list[int]], start_node: int) -> list[int]:
    visited = set()
    order = []
    
    def traverse(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                traverse(neighbor)
                
    traverse(start_node)
    return order


if __name__ == "__main__":
    g = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    assert bfs(g, 2) == [2, 0, 3, 1]
    assert dfs(g, 2) == [2, 0, 1, 3]
    print("[PASS] Level 1 Graph BFS and DFS tests passed!")
