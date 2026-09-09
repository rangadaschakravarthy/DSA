# ⚡ Master Big-O & Python Complexity Cheat Sheet

Understanding asymptotic time and space complexity is mandatory for passing technical interviews and solving competitive-programming problems.

---

## 📈 Big-O Growth Rates

```
O(1) < O(log N) < O(√N) < O(N) < O(N log N) < O(N²) < O(N³) < O(2ⁿ) < O(N!)
[Fastest / Optimal] ─────────────────────────────────────────► [Slowest / Unfeasible]
```

### Growth Rate Table for Input $N$:

| $N$ | $O(\log N)$ | $O(N)$ | $O(N \log N)$ | $O(N^2)$ | $O(2^N)$ | Target Technique |
|---|---|---|---|---|---|---|
| $10$ | $3$ operations | $10$ ops | $33$ ops | $100$ ops | $1024$ ops | Backtracking / Permutations |
| $100$ | $7$ operations | $100$ ops | $664$ ops | $10^4$ ops | Unfeasible | 2D DP / Nested Loops |
| $1,000$ | $10$ operations | $1,000$ ops | $9,965$ ops | $10^6$ ops | Unfeasible | 2D Grid DP / $O(N^2)$ algorithms |
| $10^5$ | $17$ operations | $10^5$ ops | $1.6 \times 10^6$ ops | $10^{10}$ (TLE) | Unfeasible | Sorting, Two Pointers, Hashing, Binary Search |
| $10^8$ | $27$ operations | $10^8$ ops | $2.6 \times 10^9$ (TLE) | Unfeasible | Unfeasible | Single Pass $O(N)$ or Binary Search $O(\log N)$ |

*Rule of Thumb*: Most online judges allow $\approx 10^8$ operations per second.

---

## 🐍 Python Built-in Operation Complexities

### 1. Python `list` (Dynamic Array)

| Operation | Average Time Complexity | Worst-Case Time Complexity | Explanation |
|---|---|---|---|
| `list[i]` (Access) | $O(1)$ | $O(1)$ | Direct pointer arithmetic |
| `list.append(x)` | $O(1)$ amortized | $O(N)$ | Resizing dynamic array |
| `list.pop()` (End) | $O(1)$ | $O(1)$ | Remove last element |
| `list.pop(0)` / `insert(0, x)` | $O(N)$ | $O(N)$ | Shifts all $N$ elements |
| `x in list` (Search) | $O(N)$ | $O(N)$ | Linear scan |
| `list.sort()` | $O(N \log N)$ | $O(N \log N)$ | Timsort (Hybrid Merge/Insertion sort) |
| `len(list)` | $O(1)$ | $O(1)$ | Stored length property |
| `list[a:b]` (Slice) | $O(K)$ where $K = b-a$ | $O(K)$ | Copies $K$ elements |

---

### 2. Python `dict` (Hash Table) & `set` (Hash Set)

| Operation | Average Time Complexity | Worst-Case Time Complexity | Explanation |
|---|---|---|---|
| `key in dict` / `x in set` | $O(1)$ | $O(N)$ | Hash table lookup |
| `dict[key] = val` / `set.add(x)` | $O(1)$ | $O(N)$ | Hash insert |
| `del dict[key]` / `set.remove(x)` | $O(1)$ | $O(N)$ | Hash deletion |
| `dict.keys()` / `values()` | $O(N)$ | $O(N)$ | Creates view over elements |

---

### 3. Python `collections.deque` (Double-Ended Queue)

| Operation | Average Time Complexity | Explanation |
|---|---|---|
| `deque.append(x)` | $O(1)$ | Add to right end |
| `deque.appendleft(x)` | $O(1)$ | Add to left end |
| `deque.pop()` | $O(1)$ | Pop from right end |
| `deque.popleft()` | $O(1)$ | Pop from left end |
| `deque[i]` (Random Access) | $O(N)$ | Doubly linked list traversal |

---

### 4. Python `heapq` (Min-Heap)

| Operation | Time Complexity | Explanation |
|---|---|---|
| `heapq.heapify(list)` | $O(N)$ | Builds heap in-place (Floyd's algorithm) |
| `heapq.heappush(heap, item)` | $O(\log N)$ | Sift-up insertion |
| `heapq.heappop(heap)` | $O(\log N)$ | Sift-down removal of minimum element |
| `heap[0]` (Peek Min) | $O(1)$ | Inspect root element |
| `heapq.heappushpop(heap, item)`| $O(\log N)$ | Optimized push followed by pop |

---

## 🧠 Memory & Space Complexity Guide

- **$O(1)$ Auxiliary Space**: Modifying inputs in-place using simple pointers/variables.
- **$O(N)$ Auxiliary Space**: Creating auxiliary lists, hash maps, or recursion stacks of depth $N$.
- **Call Stack Memory**: Every recursive function call consumes call stack memory proportional to the maximum depth of the recursion tree.
  - Recursion depth of $N \implies O(N)$ stack space.
  - Balanced binary tree recursion depth $\log N \implies O(\log N)$ stack space.
