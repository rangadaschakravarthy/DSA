"""
Level 2: Number of Islands

Problem:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

Time Complexity: O(M * N)
Space Complexity: O(M * N) worst case recursion
"""

def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
        
    m, n = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
                
    return islands


if __name__ == "__main__":
    g1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    assert num_islands(g1) == 1
    
    g2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    assert num_islands(g2) == 3
    print("[PASS] Level 2 Number of Islands tests passed!")
