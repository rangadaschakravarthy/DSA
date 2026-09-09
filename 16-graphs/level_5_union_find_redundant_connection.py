"""
Level 5: Union-Find & Redundant Connection

Problem:
Given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
Find an edge that can be removed so that the resulting graph is a tree of n nodes.

Time Complexity: O(N * alpha(N)) ~ O(N)
Space Complexity: O(N)
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.parent[rootY] = rootX
        self.rank[rootX] += self.rank[rootY]
        return True


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    uf = UnionFind(len(edges))
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []


if __name__ == "__main__":
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("[PASS] Level 5 Union-Find & Redundant Connection tests passed!")
