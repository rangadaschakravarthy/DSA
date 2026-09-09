# Topic 16: Graph Algorithms (Level 1 to Level 9)

Graphs are collections of nodes (vertices) connected by edges (directed or undirected, weighted or unweighted). Master traversals (BFS, DFS), cycle detection, topological sort, shortest paths, and Disjoint Set Union (DSU).

---

## Level-1: Graph BFS and DFS Traversals

### Question
Implement Breadth-First Search (BFS) and Depth-First Search (DFS) traversals on an adjacency list graph.

### Description / Explanation
- **BFS**: Level-by-level exploration using a Queue.
- **DFS**: Deepest path exploration using Recursion / Stack.

### Logic / Approach
Track visited set to prevent infinite loops in cyclic graphs.

### Sample Input & Output
- **Input**: `graph = {0:[1,2], 1:[2], 2:[0,3], 3:[3]}`, `start = 2`
- **Output**: `BFS = [2, 0, 3, 1]`, `DFS = [2, 0, 1, 3]`

### Explanation
BFS explores 2's direct neighbors first; DFS dives into depth.

### Python Implementation
- [`level_1_graph_bfs_dfs.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_1_graph_bfs_dfs.py)

---

## Level-2: Number of Islands

### Question
Count the number of connected components of land `'1'`s in a 2D binary grid.

### Description / Explanation
Connected component counting using DFS / BFS.

### Logic / Approach
Traverse grid: when encountering `'1'`, increment island count and trigger DFS to sink all connected land cells to `'0'`.

### Sample Input & Output
- **Input**: Grid with 3 isolated land clusters
- **Output**: `3`

### Explanation
3 connected components of land.

### Python Implementation
- [`level_2_number_of_islands.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_2_number_of_islands.py)

---

## Level-3: Clone Graph

### Question
Return a deep copy (clone) of a connected undirected graph.

### Description / Explanation
Graph cloning requiring reference mapping from original nodes to new cloned nodes.

### Logic / Approach
DFS with hash map `cloned_map: OriginalNode -> ClonedNode` to instantiate new nodes and link cloned neighbors.

### Sample Input & Output
- **Input**: Connected graph `1 <-> 2`
- **Output**: Deep copied graph with distinct node memory addresses.

### Explanation
Preserves graph structure in newly allocated memory.

### Python Implementation
- [`level_3_clone_graph.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_3_clone_graph.py)

---

## Level-4: Course Schedule I & II

### Question
Find topological ordering of courses given prerequisite dependencies `[a, b]`.

### Description / Explanation
Topological Sort on Directed Acyclic Graph (DAG) using Kahn's Algorithm.

### Logic / Approach
1. Compute in-degree of all nodes.
2. Push in-degree 0 nodes into Queue.
3. Pop node, append to topological order, decrement in-degree of neighbors, push newly 0 in-degree nodes.

### Sample Input & Output
- **Input**: `numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
- **Output**: `[0, 1, 2, 3]` (or `[0, 2, 1, 3]`)

### Explanation
Course 0 is taken first, followed by 1 and 2, and finally 3.

### Python Implementation
- [`level_4_course_schedule.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_4_course_schedule.py)

---

## Level-5: Union-Find & Redundant Connection

### Question
Find an edge that can be removed to turn a graph with $N$ nodes and $N$ edges into a tree.

### Description / Explanation
Disjoint Set Union (DSU / Union-Find) with path compression and rank.

### Logic / Approach
Iterate through edges: if `find(u) == find(v)`, adding edge `(u, v)` creates a cycle; return `[u, v]`. Else `union(u, v)`.

### Sample Input & Output
- **Input**: `edges = [[1,2], [1,3], [2,3]]`
- **Output**: `[2, 3]`

### Explanation
Removing `[2, 3]` restores tree structure.

### Python Implementation
- [`level_5_union_find_redundant_connection.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_5_union_find_redundant_connection.py)

---

## Level-6: Word Ladder

### Question
Find shortest transformation sequence length from `beginWord` to `endWord` changing 1 letter at a time.

### Description / Explanation
Unweighted Shortest Path BFS on word wildcard patterns (e.g., `h*t`).

### Logic / Approach
Build pattern dictionary `h*t -> [hot, hat]`. BFS level-by-level starting from `beginWord`.

### Sample Input & Output
- **Input**: `begin = "hit"`, `end = "cog"`, `words = ["hot","dot","dog","lot","log","cog"]`
- **Output**: `5`

### Explanation
Sequence: `"hit" -> "hot" -> "dot" -> "dog" -> "cog"` (5 words).

### Python Implementation
- [`level_6_word_ladder.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_6_word_ladder.py)

---

## Level-7: Network Delay Time (Dijkstra)

### Question
Find minimum time for signal sent from node $K$ to reach all $N$ weighted directed graph nodes.

### Description / Explanation
Dijkstra's Shortest Path Algorithm using Min-Heap (Priority Queue).

### Logic / Approach
Min-Heap storing `(dist, node)`. Continuously extract node with minimum distance and relax outbound neighbor edges.

### Sample Input & Output
- **Input**: `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2`
- **Output**: `2`

### Explanation
Signal reaches node 1 in time 1, node 3 in time 1, node 4 in time $1+1=2$. Max time $= 2$.

### Python Implementation
- [`level_7_network_delay_time_dijkstra.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_7_network_delay_time_dijkstra.py)

---

## Level-8: Cheapest Flights Within K Stops

### Question
Find cheapest flight price from `src` to `dst` with at most $K$ intermediate stops.

### Description / Explanation
Shortest path with edge-count constraint using Bellman-Ford algorithm.

### Logic / Approach
Run $K+1$ iterations relaxing all edges on temporary distance array.

### Sample Input & Output
- **Input**: `n = 3`, `flights = [[0,1,100],[1,2,100],[0,2,500]]`, `src = 0`, `dst = 2`, `k = 1`
- **Output**: `200`

### Explanation
Flight route $0 \rightarrow 1 \rightarrow 2$ costs $100 + 100 = 200$ (1 stop).

### Python Implementation
- [`level_8_cheapest_flights_k_stops.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_8_cheapest_flights_k_stops.py)

---

## Level-9: Alien Dictionary

### Question
Derive the secret alphabet character order from a sorted dictionary of alien words.

### Description / Explanation
Advanced Topological Sort handling invalid prefix edge cases.

### Logic / Approach
Compare adjacent sorted words to find first differing character pair `w1[j] -> w2[j]`. Run Kahn's BFS. Detect cycle if output length $\ne$ unique characters count.

### Sample Input & Output
- **Input**: `words = ["wrt","wrf","er","ett","rftt"]`
- **Output**: `"wertf"`

### Explanation
Relative ordering derived: `w -> e -> r -> t -> f`.

### Python Implementation
- [`level_9_alien_dictionary.py`](file:///c:/Users/chakr/Downloads/DSA/16-graphs/level_9_alien_dictionary.py)
