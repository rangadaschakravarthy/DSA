# 📅 30-Day Intensive DSA Mastery Plan

A structured, 4-week roadmap designed to take you from foundational syntax to solving unseen interview and competitive-programming problems independently.

---

## 🗓️ Overview Schedule

```
Week 1: Core Problem Solving Foundations (Arrays, Hashing, Pointers, Windows, Stacks)
Week 2: Linear & Hierarchical Data Structures (Lists, Recursion, Binary Search, Trees, Heaps)
Week 3: Advanced Optimization & Graphs (Greedy, Intervals, BFS/DFS, Topo Sort, Backtracking)
Week 4: Dynamic Programming Mastery & Final Assessments (1D/2D DP, Knapsack, Mock Interview)
```

---

## 🟩 WEEK 1 — Core Problem Solving Foundations

### Day 1 — Big-O Notation & Array Fundamentals
- **Theory**: Big-O, Time vs Space complexity, Python list internal memory, single-pass traversals.
- **Goal**: Master Level 1 & Level 2 basic traversal operations.
- **Problems**:
  1. [`01_find_maximum.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level-1/01_find_maximum.py) (Level 1, Easy)
  2. [`02_find_minimum.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level-1/02_find_minimum.py) (Level 1, Easy)
  3. [`03_sum_array.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level-1/03_sum_array.py) (Level 1, Easy)
  4. [`04_reverse_array.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-1/04_reverse_array.py) (Level 1, Easy)
  5. [`05_second_largest.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-2/05_second_largest.py) (Level 2, Easy)
  6. [`06_remove_duplicates_sorted.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-2/06_remove_duplicates_sorted.py) (Level 2, Easy)
  7. [`07_move_zeroes.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-2/07_move_zeroes.py) (Level 2, Easy)
  8. [`08_rotate_array.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-3/08_rotate_array.py) (Level 3, Medium)

---

### Day 2 — Subarrays & Prefix Sum Patterns
- **Theory**: Cumulative sums, Prefix sum arrays, Kadane's Algorithm for max subarray sum.
- **Goal**: Transition from $O(N^2)$ brute force to $O(N)$ single pass.
- **Problems**:
  1. [`01_running_sum.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-2/01_running_sum.py) (Level 2, Easy)
  2. [`02_range_sum_query.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-3/02_range_sum_query.py) (Level 3, Easy)
  3. [`03_maximum_subarray_kadane.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-3/03_maximum_subarray_kadane.py) (Level 3, Medium)
  4. [`04_best_time_stock.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-3/04_best_time_stock.py) (Level 3, Easy)
  5. [`05_majority_element_boyer_moore.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level-4/05_majority_element_boyer_moore.py) (Level 4, Medium)

---

### Day 3 — Hashing & Frequency Map Optimization
- **Theory**: Hash functions, $O(1)$ lookups, `dict`, `set`, `Counter`, Prefix Sum + Hash Map.
- **Goal**: Trade $O(N)$ space to eliminate nested linear loops.
- **Problems**:
  1. [`01_two_sum.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level-2/01_two_sum.py) (Level 2, Easy)
  2. [`02_contains_duplicate.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level-1/02_contains_duplicate.py) (Level 1, Easy)
  3. [`03_valid_anagram.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level-2/03_valid_anagram.py) (Level 2, Easy)
  4. [`04_first_unique_character.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level-2/04_first_unique_character.py) (Level 2, Easy)
  5. [`05_subarray_sum_equals_k.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level-4/05_subarray_sum_equals_k.py) (Level 4, Medium)
  6. [`06_longest_consecutive_sequence.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level-5/06_longest_consecutive_sequence.py) (Level 5, Medium)

---

### Day 4 — Two Pointers Technique
- **Theory**: Opposite pointers, Fast & Slow pointers, In-place array mutation.
- **Goal**: Reduce space complexity to $O(1)$ on sorted or structured inputs.
- **Problems**:
  1. [`01_two_sum_sorted.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level-2/01_two_sum_sorted.py) (Level 2, Easy)
  2. [`02_valid_palindrome.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level-2/02_valid_palindrome.py) (Level 2, Easy)
  3. [`03_container_with_most_water.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level-4/03_container_with_most_water.py) (Level 4, Medium)
  4. [`04_three_sum.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level-4/04_three_sum.py) (Level 4, Medium)
  5. [`05_trapping_rain_water.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level-7/05_trapping_rain_water.py) (Level 7, Hard)

---

### Day 5 — Sliding Window Pattern
- **Theory**: Fixed-size vs Variable-size windows, Maintaining window invariant.
- **Goal**: Process continuous contiguous subsegment constraints in $O(N)$ time.
- **Problems**:
  1. [`01_max_sum_subarray_k.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level-2/01_max_sum_subarray_k.py) (Level 2, Easy)
  2. [`02_longest_substring_without_repeats.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level-4/02_longest_substring_without_repeats.py) (Level 4, Medium)
  3. [`03_min_size_subarray_sum.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level-4/03_min_size_subarray_sum.py) (Level 4, Medium)
  4. [`04_longest_repeating_character_replacement.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level-5/04_longest_repeating_character_replacement.py) (Level 5, Medium)
  5. [`05_minimum_window_substring.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level-8/05_minimum_window_substring.py) (Level 8, Hard)

---

### Day 6 — Strings & Monotonic Stack Foundations
- **Theory**: LIFO principle, Matching parentheses, Monotonic stack invariants.
- **Goal**: Solve nearest smaller/greater element problems in $O(N)$.
- **Problems**:
  1. [`01_valid_parentheses.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level-2/01_valid_parentheses.py) (Level 2, Easy)
  2. [`02_min_stack.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level-3/02_min_stack.py) (Level 3, Medium)
  3. [`03_eval_rpn.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level-4/03_eval_rpn.py) (Level 4, Medium)
  4. [`04_next_greater_element.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level-5/04_next_greater_element.py) (Level 5, Medium)
  5. [`05_daily_temperatures.py`](file:///c:/Users/chakr/Downloads/DSA/06-stack/level-5/05_daily_temperatures.py) (Level 5, Medium)

---

### Day 7 — Pattern-Agnostic Revision 1
> **CRITICAL RULE**: Pattern tags are intentionally omitted. You must analyze problem constraints and select the pattern yourself.

- **Challenge 1**: [Mixed Challenge A] Solve subarray sum divisibility by K.
- **Challenge 2**: [Mixed Challenge B] Find longest subarray with equal 0s and 1s.
- **Challenge 3**: [Mixed Challenge C] Remove all adjacent duplicates in string II.

---

## 🟦 WEEK 2 — Core Data Structures

### Day 8 — Linked List Pointers
- **Theory**: Nodes, Single/Doubly linked lists, Fast & Slow pointers, In-place reversal.
- **Problems**: Reverse Linked List, Middle of Linked List, Linked List Cycle, Merge Two Sorted Lists, Reorder List.

### Day 9 — Recursion & Divide and Conquer
- **Theory**: Base cases, Call stack memory, Recurrence relations, Subproblem decomposition.
- **Problems**: Fibonacci Memoized, Power(x, n), Reverse String Recursive, Merge Sort Implementation.

### Day 10 — Binary Search & Search Space Optimization
- **Theory**: Monotonic space, Boundary conditions (`low <= high`), Binary Search on Answer.
- **Problems**: Standard Binary Search, Search Insert Position, Find First & Last Occurrence, Search in Rotated Sorted Array, Capacity to Ship Packages.

### Day 11 — Binary Trees & Traversal Algorithms
- **Theory**: Tree properties, DFS (Preorder, Inorder, Postorder), BFS Level Order.
- **Problems**: Max Depth of Tree, Invert Binary Tree, Level Order Traversal, Diameter of Tree, Lowest Common Ancestor.

### Day 12 — Binary Search Tree (BST) Properties
- **Theory**: BST Invariant ($Left < Root < Right$), Inorder traversal sorting property.
- **Problems**: Validate BST, Search in BST, K-th Smallest Element in BST, Insert/Delete Node in BST.

### Day 13 — Heaps & Priority Queues
- **Theory**: Binary Min/Max Heap structure, `heapq` module operations ($O(N)$ heapify, $O(\log N)$ push/pop).
- **Problems**: Kth Largest Element in Array, Top K Frequent Elements, Merge K Sorted Lists, Find Median from Data Stream.

### Day 14 — Pattern-Agnostic Revision 2
- **Mixed Challenge Suite**: 5 Pattern-hidden tree, heap, and pointer manipulation problems.

---

## 🟨 WEEK 3 — Advanced Problem Solving & Graphs

### Day 15 — Greedy Algorithms & Proofs
- **Theory**: Local optimum choice, Exchange arguments, Sorting + Greedy heuristics.
- **Problems**: Assign Cookies, Jump Game I & II, Gas Station, Task Scheduler.

### Day 16 — Interval Scheduling & Sweep-Line
- **Theory**: Sorting intervals by start/end time, Overlap conditions, Difference arrays.
- **Problems**: Merge Intervals, Insert Interval, Non-overlapping Intervals, Meeting Rooms II.

### Day 17 — Graph Fundamentals (BFS & DFS)
- **Theory**: Adjacency Lists, Graph traversals, Cycle detection, Connected components.
- **Problems**: Number of Islands, Flood Fill, Clone Graph, Max Area of Island.

### Day 18 — Graph Algorithms & Union-Find
- **Theory**: Disjoint Set Union (DSU) with Path Compression, Topological Sorting (Kahn's BFS / DFS).
- **Problems**: Course Schedule I & II, Redundant Connection, Graph Valid Tree, Number of Connected Components.

### Day 19 — Backtracking & State Space Search
- **Theory**: Decision trees, Choose-Explore-Undo state management, Pruning invalid paths.
- **Problems**: Subsets I & II, Permutations, Combination Sum, Word Search, N-Queens.

### Day 20 — Shortest Path & Advanced Graph Algorithms
- **Theory**: Weighted graphs, Dijkstra's Single Source Shortest Path with Min-Heap ($O((V+E)\log V)$).
- **Problems**: Network Delay Time, Path with Minimum Effort, Cheapest Flights Within K Stops.

### Day 21 — Pattern-Agnostic Revision 3
- **Mixed Challenge Suite**: 5 Unlabeled Graph, Greedy, and Backtracking problems.

---

## 🟥 WEEK 4 — Dynamic Programming & Assessment

### Day 22 — DP Foundations (Recursion to Tabulation)
- **Theory**: Overlapping subproblems, Optimal substructure, Top-Down Memoization vs Bottom-Up Tabulation, Space optimization.
- **Problems**: Climbing Stairs, Min Cost Climbing Stairs, House Robber I & II.

### Day 23 — 1D Dynamic Programming
- **Theory**: DP state definitions, Recurrence formulation, Past-window state tracking.
- **Problems**: Decode Ways, Coin Change I, Word Break, Maximum Product Subarray.

### Day 24 — Knapsack Problems (0/1 & Unbounded)
- **Theory**: Capacity-based decision states, Item inclusion/exclusion logic.
- **Problems**: Partition Equal Subset Sum, Target Sum, Unbounded Coin Change II, Rod Cutting.

### Day 25 — Subsequence & String DP
- **Theory**: 2D grid DP states (`dp[i][j]` representing prefixes of strings).
- **Problems**: Longest Common Subsequence (LCS), Longest Increasing Subsequence (LIS), Edit Distance, Distinct Subsequences.

### Day 26 — Grid Dynamic Programming
- **Theory**: Matrix movement states, Boundary base cases, Minimum/Maximum path cost accumulators.
- **Problems**: Unique Paths I & II, Minimum Path Sum, Triangle, Dungeon Game.

### Day 27 — Advanced DP Patterns (Interval & State Machine DP)
- **Theory**: Subsegment range DP (`dp[i][j]` over range $[i..j]$), State machine transitions.
- **Problems**: Longest Palindromic Substring, Best Time to Buy/Sell Stock with Cooldown/Fee.

### Day 28 — Dynamic Programming Revision
- Comprehensive review of all 6 core DP state formulations.

---

### Day 29 — The 10-Problem Unseen Mock Interview
> **Simulated Technical Interview**: 10 completely pattern-hidden problems. You must determine topic, pattern, space/time complexity, implement clean Python code, and pass all edge case tests independently.

---

### Day 30 — Final Assessment & Mastery Benchmark
- Final evaluation across all 19 topics and 9 difficulty levels. Benchmark your readiness for FAANG / Top Tier Competitive Programming.
