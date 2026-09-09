"""
Level 1: Graph BFS & DFS Traversals

Topics Covered:
1. Number of Islands (2D Grid DFS O(M * N))
2. Shortest Path in Unweighted Graph (BFS O(V + E))

Complexity:
- Number of Islands: O(M * N) time, O(M * N) space.
- BFS Shortest Path: O(V + E) time, O(V) space.
"""

from collections import deque, defaultdict

def num_islands(grid: list[list[str]]) -> int:
    """
    Counts number of islands (connected components of '1's) in a 2D binary grid.
    """
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # Mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
                
    return islands


def shortest_path_unweighted(n: int, edges: list[list[int]], start: int, target: int) -> int:
    """
    Finds shortest path distance from start to target in an unweighted undirected graph using BFS.
    Returns -1 if unreachable.
    """
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist
            
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                
    return -1


if __name__ == "__main__":
    # Test Number of Islands
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert num_islands(grid1) == 1
    
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert num_islands(grid2) == 3
    
    # Test Shortest Path BFS
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
    assert shortest_path_unweighted(5, edges, 0, 4) == 3  # 0 -> 1 -> 3 -> 4
    
    print("[SUCCESS] All Level 1 Graph Traversals tests passed!")
