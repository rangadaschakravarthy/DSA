"""
Level 2: Topological Sorting & Directed Acyclic Graphs (DAG)

Topics Covered:
1. Course Schedule I (Cycle Detection in Directed Graph O(V + E))
2. Course Schedule II (Topological Order via Kahn's Algorithm BFS O(V + E))

Kahn's Algorithm (BFS In-degree Approach):
1. Compute in-degree (number of incoming edges) for every node.
2. Push all nodes with in-degree 0 into a queue.
3. Pop from queue, add to topological order, and decrement in-degree of neighbors.
4. If in-degree becomes 0, push neighbor to queue.
5. If topological order contains all V nodes, graph is DAG. Else, cycle exists!
"""

from collections import deque, defaultdict

def can_finish_courses(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Checks if you can finish all courses given prerequisite dependencies.
    """
    in_degree = [0] * num_courses
    adj = defaultdict(list)
    
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
        
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    completed_count = 0
    
    while queue:
        node = queue.popleft()
        completed_count += 1
        
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    return completed_count == num_courses


def find_course_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Returns valid topological order of courses. Returns [] if cycle exists.
    """
    in_degree = [0] * num_courses
    adj = defaultdict(list)
    
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
        
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    return topo_order if len(topo_order) == num_courses else []


if __name__ == "__main__":
    # Test Course Schedule I
    assert can_finish_courses(2, [[1, 0]]) is True
    assert can_finish_courses(2, [[1, 0], [0, 1]]) is False
    
    # Test Course Schedule II
    order = find_course_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert order in [[0, 1, 2, 3], [0, 2, 1, 3]]
    
    print("[SUCCESS] All Level 2 Topological Sort tests passed!")
