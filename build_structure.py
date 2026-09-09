import os
import json

root_dir = r"c:\Users\chakr\Downloads\DSA"

topics = [
    ("00-fundamentals", "Fundamentals & Math", "Big-O, Modular Arithmetic, Bit Manipulation, Sieve, GCD/LCM"),
    ("01-arrays", "Arrays", "Subarrays, Prefix Sum, Kadane's Algorithm, 2D Matrices, Dutch Flag"),
    ("02-strings", "Strings", "Character Frequency, Substrings, Palindromes, Matching, KMP"),
    ("03-hashing", "Hashing", "Hash Tables, Frequency Maps, Prefix Sum + Map, Grouping"),
    ("04-two-pointers", "Two Pointers", "Opposite Pointers, Fast/Slow Pointers, Partitioning"),
    ("05-sliding-window", "Sliding Window", "Fixed Window, Variable Window, At Most K Patterns"),
    ("06-stack", "Stack", "LIFO, Expression Parsing, Monotonic Stack, Histogram"),
    ("07-queue", "Queue & Deque", "FIFO, Sliding Window Maximum, Monotonic Queue"),
    ("08-linked-list", "Linked List", "Pointer Manipulation, Fast/Slow Pointers, Cycle Entry, Reversal"),
    ("09-recursion", "Recursion", "Base Cases, Call Stack, Divide & Conquer, Tree Recursion"),
    ("10-binary-search", "Binary Search", "Monotonic Search Space, Rotated Arrays, Search on Answer"),
    ("11-trees", "Binary Trees", "DFS/BFS Traversals, Height, Path Sums, LCA, Tree DP"),
    ("12-bst", "Binary Search Trees", "BST Invariant, Validation, Range Queries, Kth Smallest"),
    ("13-heap", "Heap & Priority Queue", "Min/Max Heap, Top-K Elements, Two Heaps Median"),
    ("14-greedy", "Greedy Algorithms", "Local vs Global Optimum, Exchange Arguments, Scheduling"),
    ("15-intervals", "Intervals", "Sort-Compare-Merge, Meeting Rooms, Sweep-Line"),
    ("16-graphs", "Graphs", "BFS/DFS, Topological Sort, Union-Find, Dijkstra, Shortest Paths"),
    ("17-backtracking", "Backtracking", "Choose-Explore-Undo, Subsets, Permutations, N-Queens"),
    ("18-dynamic-programming", "Dynamic Programming", "Memoization, Tabulation, 1D/2D DP, Knapsack, LCS, LIS")
]

levels = [
    ("level-1", "Level 1 — Absolute Beginner", "Easy"),
    ("level-2", "Level 2 — Beginner", "Easy"),
    ("level-3", "Level 3 — Pattern Recognition", "Easy → Medium"),
    ("level-4", "Level 4 — Intermediate", "Medium"),
    ("level-5", "Level 5 — Strong Intermediate", "Medium → Hard"),
    ("level-6", "Level 6 — Advanced", "Hard"),
    ("level-7", "Level 7 — Expert", "Hard"),
    ("level-8", "Level 8 — Interview / Competitive Programming", "Hard / Very Hard"),
    ("level-9", "Level 9 — Mastery", "Very Hard / Expert")
]

# Ensure directory structure exists for all 19 topics and 9 levels
for topic_folder, topic_title, topic_desc in topics:
    topic_path = os.path.join(root_dir, topic_folder)
    os.makedirs(topic_path, exist_ok=True)
    for lvl_folder, _, _ in levels:
        os.makedirs(os.path.join(topic_path, lvl_folder), exist_ok=True)

print("Created all 19 topic folders with 9 level subdirectories each.")
