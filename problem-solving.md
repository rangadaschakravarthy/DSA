# 🧠 Master Problem-Solving Framework

> **Specifically written for students who say:**  
> *"I understand the solution when someone explains it, but I cannot solve unseen problems independently."*

---

## 🎯 Why You Struggle with Unseen Problems

If you struggle with unseen problems, it is usually because you are trying to **jump directly from reading the problem to writing Python code**. This skips the crucial intermediate phase: **Systematic Problem Deconstruction**.

Competitive programmers and senior engineers do not memorize solutions. They use a **repeatable 7-step process** that forces the optimal pattern to emerge logically.

---

## 🛠️ The 7-Step Repeatable Framework

```
Step 1: Understand Constraints & Inputs
                  │
                  ▼
Step 2: Formulate Brute-Force Solution (N2, N3)
                  │
                  ▼
Step 3: Pinpoint the Bottleneck ("What makes this slow?")
                  │
                  ▼
Step 4: Match Clues to Algorithmic Patterns
                  │
                  ▼
Step 5: Define Invariant & Optimize
                  │
                  ▼
Step 6: Write Clean Pseudocode / Python
                  │
                  ▼
Step 7: Test with Critical Edge Cases
```

---

### Step 1 — Understand & Deconstruct Inputs

Before touching code, answer these 4 questions explicitly:
1. **What are the exact inputs and types?** (Array of integers? String? Graph edges?)
2. **What is the expected output?** (Single integer? Subarray? Boolean flag?)
3. **What are the numerical constraints?**
   - $N \le 20 \implies O(2^N)$ or $O(N!)$ (Backtracking / Bitmask)
   - $N \le 10^3 \implies O(N^2)$ (Nested loops / 2D DP)
   - $N \le 10^5 \implies O(N \log N)$ or $O(N)$ (Sorting, Two Pointers, Hashing, Binary Search)
   - $N \le 10^9 \implies O(\log N)$ or $O(1)$ (Binary Search, Math)
4. **Are there non-obvious constraints?** (Negative numbers? Duplicates? Empty arrays? Unsorted input?)

---

### Step 2 — Formulate the Brute Force

Always start by asking:
> *"What is the absolute simplest, most naive way to solve this problem if time complexity did not matter?"*

- If asked for a subarray, generate all $O(N^2)$ or $O(N^3)$ subarrays.
- If asked for pairs, check all $O(N^2)$ pairs.
- If asked for paths, generate all possibilities recursively.

**Rule**: Never skip brute force. Brute force proves you understand what the problem is asking!

---

### Step 3 — Find the Bottleneck

Ask yourself:
> *"What specific operation is making my brute force slow?"*

Examples of bottlenecks:
- *"I am repeatedly scanning the array to find a target value."* $\implies$ Redundant linear search.
- *"I am recomputing the sum of overlapping subarrays."* $\implies$ Redundant summation.
- *"I am checking if an element exists by iterating through a list."* $\implies$ $O(N)$ lookup cost.

---

### Step 4 — Match Clues to Algorithmic Patterns

Use the **Pattern Recognition Clue Matrix**:

| Problem Statement Clue | Potential Bottleneck | Matching Pattern |
|---|---|---|
| Input array is **Sorted** | Linear search is $O(N)$ | **Two Pointers** or **Binary Search** |
| Find a **Pair / Triplet** with target sum | $O(N^2)$ nested loops | **Hash Map** or **Sorted Two Pointers** |
| Continuous **Subarray with sum / max / condition** | Recalculating range sum $O(N^2)$ | **Sliding Window** or **Prefix Sum** |
| Find **Next Greater / Smaller** element | Comparing right elements $O(N^2)$ | **Monotonic Stack** |
| Find **Top K / K-th Largest** elements | Sorting entire array $O(N \log N)$ | **Min-Heap / Max-Heap** ($O(N \log K)$) |
| Find **Shortest Path** in unweighted graph | Exhaustive recursive search | **BFS (Breadth-First Search)** |
| **All combinations / permutations / subsets** | Checking all invalid branches | **Backtracking (Choose-Explore-Undo)** |
| Overlapping **Subproblems / Optimal Substructure** | Recomputing recursive states | **Dynamic Programming (Memoization / DP)** |
| Minimum capacity / Maximum minimum value | Discrete answer range search | **Binary Search on Answer** |
| Range query sum updates | Recalculating range sums | **Difference Array / Prefix Sum** |

---

### Step 5 — Formulate the Algorithmic Invariant & Optimize

An **Invariant** is a mathematical condition that remains true throughout the execution of your algorithm.

- **Two Pointers Invariant**: "Elements outside $[left, right]$ are guaranteed to be invalid."
- **Sliding Window Invariant**: "The range $[L, R]$ always satisfies the target condition."
- **Binary Search Invariant**: "The optimal answer is guaranteed to lie within range $[low, high]$."
- **Monotonic Stack Invariant**: "Elements in stack are strictly decreasing in value."

Using your invariant, replace repeated work with:
- $O(1)$ Hash Map lookups.
- $O(\log N)$ Binary Search / Heap updates.
- Dynamic Programming memoization tables.

---

### Step 6 — Implement in Python

Write clean, readable Python code:
- Use clear variable names (`left`, `right`, `window_sum`, `seen_map`).
- Avoid multi-line nested ternaries or obscure index math.
- Add brief comments explaining *why* decisions are made, not just syntax.

---

### Step 7 — Test & Verify Edge Cases

Dry-run your code step-by-step against critical edge cases:
1. **Empty input / single-element input** (`nums = []` or `nums = [5]`)
2. **All duplicate values** (`nums = [2, 2, 2, 2]`)
3. **All negative numbers** (`nums = [-5, -2, -9]`)
4. **Target does not exist / No valid subarray**
5. **Array already sorted vs reverse sorted**

---

## 🔁 The Three-Attempt Rule

When practicing:

1. **Attempt 1 (25 mins)**: Try to solve completely independently using the 7-Step Framework.
2. **Attempt 2 (15 mins)**: If stuck, read **Hint 1 & Hint 2** in the problem file.
3. **Attempt 3 (Study & Reimplement)**: Read the complete optimal approach and Python code. Close the file, wait 10 minutes, and **re-implement the solution from scratch** without looking.

---

## ☀️ Daily Study Workflow

```
Read Concept & Invariants ──► Solve Level 1-2 Warmups ──► Solve Level 3-4 Patterns
                                                                   │
Review Mistakes & Update Log ◄── Write Pattern Notes ◄── Attempt Level 5+ Challenges
```
