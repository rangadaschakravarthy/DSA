"""
Level 4: Course Schedule I & II (Topological Sort / Kahn's Algorithm)

Problem:
There are numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given prerequisites array where prerequisites[i] = [a, b] indicates you must take course b first.
1. Course Schedule I: Can you finish all courses?
2. Course Schedule II: Return the ordering of courses you should take.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""
from collections import deque, defaultdict

def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
        
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    return topo_order if len(topo_order) == numCourses else []


if __name__ == "__main__":
    assert find_order(2, [[1, 0]]) == [0, 1]
    assert len(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])) == 4
    assert find_order(2, [[1, 0], [0, 1]]) == []
    print("[PASS] Level 4 Course Schedule tests passed!")
