"""
Level 3: Disjoint Set Union (DSU / Union-Find)

Topics Covered:
1. Disjoint Set Union Data Structure with Path Compression & Union by Rank O(alpha(N))
2. Graph Valid Tree Verification O(V * alpha(V))

Complexity:
- Find / Union: Amortized O(alpha(N)) ≈ O(1) where alpha is Inverse Ackermann function.
- Space Complexity: O(N) parent and rank arrays.
"""

class UnionFind:
    """Disjoint Set Union data structure with path compression and rank optimization."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, i: int) -> int:
        """Finds representative of set containing i with path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        """Unites sets containing i and j. Returns False if already in same set (cycle detected)."""
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return False  # Already connected -> Union fails (cycle)
            
        # Union by rank
        if self.rank[root_i] < self.rank[root_j]:
            root_i, root_j = root_j, root_i
        self.parent[root_j] = root_i
        if self.rank[root_i] == self.rank[root_j]:
            self.rank[root_i] += 1
            
        self.components -= 1
        return True


def valid_tree(n: int, edges: list[list[int]]) -> bool:
    """
    Checks if edges form a valid tree with n nodes.
    Tree Properties:
    1. Exactly n - 1 edges.
    2. No cycles.
    3. Fully connected (single component).
    """
    if len(edges) != n - 1:
        return False
        
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return False  # Cycle detected
            
    return uf.components == 1


if __name__ == "__main__":
    # Test DSU & Graph Valid Tree
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False  # Cycle [1,2,3]
    
    print("[SUCCESS] All Level 3 Union-Find tests passed!")
