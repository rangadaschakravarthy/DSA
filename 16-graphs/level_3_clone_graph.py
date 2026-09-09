"""
Level 3: Clone Graph

Problem:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Time Complexity: O(V + E)
Space Complexity: O(V) visited map
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    if not node:
        return None
        
    cloned_map = {}
    
    def dfs(curr):
        if curr in cloned_map:
            return cloned_map[curr]
            
        copy = Node(curr.val)
        cloned_map[curr] = copy
        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs(neighbor))
            
        return copy

    return dfs(node)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors.append(n2)
    n2.neighbors.append(n1)
    
    cloned = clone_graph(n1)
    assert cloned.val == 1
    assert len(cloned.neighbors) == 1
    assert cloned.neighbors[0].val == 2
    assert cloned is not n1
    print("[PASS] Level 3 Clone Graph tests passed!")
