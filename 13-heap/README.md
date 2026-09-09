# Topic 13: Heap / Priority Queue (Level 1 to Level 9)

A Heap (Priority Queue) is a specialized tree-based data structure that satisfies the heap property: in a Min-Heap, parent node $\le$ child nodes; in a Max-Heap, parent node $\ge$ child nodes.

---

## Level-1: Heap Basics and Operations

### Question
Implement basic Min-Heap operations: heapify, push, and pop.

### Description / Explanation
Python `heapq` module provides standard $O(\log N)$ push/pop and $O(N)$ heapify.

### Logic / Approach
Heapify builds heap in linear time; popping repeatedly returns sorted elements.

### Sample Input & Output
- **Input**: `[5, 3, 8, 1, 2]`
- **Output**: `[1, 2, 3, 5, 8]`

### Explanation
Pops elements in ascending order.

### Python Implementation
- [`level_1_heap_basics.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_1_heap_basics.py)

---

## Level-2: Kth Largest Element in an Array

### Question
Find the $K$-th largest element in an unsorted array.

### Description / Explanation
Use a Min-Heap of fixed size $K$.

### Logic / Approach
Maintain size $K$ heap: when heap grows $> K$, pop top (smallest). At end, top of heap is $K$-th largest.

### Sample Input & Output
- **Input**: `nums = [3,2,1,5,6,4]`, `k = 2`
- **Output**: `5`

### Explanation
2nd largest element is 5.

### Python Implementation
- [`level_2_kth_largest_element.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_2_kth_largest_element.py)

---

## Level-3: K Closest Points to Origin

### Question
Find $K$ points on 2D plane closest to origin $(0,0)$.

### Description / Explanation
Euclidean distance metric $x^2 + y^2$.

### Logic / Approach
Max-Heap of size $K$ storing `(-distance, x, y)` to drop farthest points whenever size $> K$.

### Sample Input & Output
- **Input**: `points = [[1,3], [-2,2]]`, `k = 1`
- **Output**: `[[-2, 2]]`

### Explanation
Distance of `[1,3]` is 10, distance of `[-2,2]` is 8 $\rightarrow$ `[-2,2]` is closer.

### Python Implementation
- [`level_3_k_closest_points.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_3_k_closest_points.py)

---

## Level-4: Task Scheduler

### Question
Find minimum CPU clock intervals to execute tasks given cooldown $N$ between identical tasks.

### Description / Explanation
Most frequent task dictates frame structure.

### Logic / Approach
Calculate bottleneck: $(max\_freq - 1) \times (n + 1) + max\_count$.

### Sample Input & Output
- **Input**: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
- **Output**: `8`

### Explanation
Execution order: `A -> B -> idle -> A -> B -> idle -> A -> B` (8 units).

### Python Implementation
- [`level_4_task_scheduler.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_4_task_scheduler.py)

---

## Level-5: Reorganize String

### Question
Rearrange characters in string so no two adjacent characters are identical.

### Description / Explanation
Max-Heap based on character frequencies.

### Logic / Approach
Pop top two most frequent characters, append to result, decrement frequencies, and push back.

### Sample Input & Output
- **Input**: `s = "aab"`
- **Output**: `"aba"`

### Explanation
No adjacent identical characters.

### Python Implementation
- [`level_5_reorganize_string.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_5_reorganize_string.py)

---

## Level-6: Find Median from Data Stream

### Question
Support stream insertions and median queries in $O(\log N)$ and $O(1)$ time respectively.

### Description / Explanation
Two Heaps balance strategy: Max-Heap (lower half) + Min-Heap (upper half).

### Logic / Approach
Keep heap size difference $\le 1$. Median is average of tops (if even) or top of larger heap (if odd).

### Sample Input & Output
- **Input**: `add(1)`, `add(2)`, `findMedian()`, `add(3)`, `findMedian()`
- **Output**: `1.5`, `2.0`

### Explanation
Stream `[1, 2]` median is 1.5; stream `[1, 2, 3]` median is 2.0.

### Python Implementation
- [`level_6_median_data_stream.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_6_median_data_stream.py)

---

## Level-7: Merge K Sorted Lists / Arrays using Heap

### Question
Merge $K$ pre-sorted arrays into a single sorted array.

### Description / Explanation
Min-Heap storing tuple `(val, array_index, element_index)`.

### Logic / Approach
Pop smallest element, append to result, and insert next element from the same list into min-heap.

### Sample Input & Output
- **Input**: `lists = [[1, 4, 5], [1, 3, 4], [2, 6]]`
- **Output**: `[1, 1, 2, 3, 4, 4, 5, 6]`

### Explanation
Performs efficient $K$-way merge in $O(N \log K)$ time.

### Python Implementation
- [`level_7_merge_k_sorted_lists_heap.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_7_merge_k_sorted_lists_heap.py)

---

## Level-8: Smallest Range Covering Elements from K Lists

### Question
Find smallest range $[a, b]$ containing at least one element from each of $K$ sorted lists.

### Description / Explanation
Maintain a Min-Heap of current candidate elements from each list while tracking `max_val`.

### Logic / Approach
Pop minimum element, compute range `[min_val, max_val]`, advance pointer in popped element's list.

### Sample Input & Output
- **Input**: `[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]`
- **Output**: `[20, 24]`

### Explanation
Includes 24 (list 1), 20 (list 2), 22 (list 3). Range width $= 4$.

### Python Implementation
- [`level_8_smallest_range_k_lists.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_8_smallest_range_k_lists.py)

---

## Level-9: IPO (Maximize Capital with K Projects)

### Question
Given initial capital $W$, choose up to $K$ distinct projects to maximize capital.

### Description / Explanation
Min-Heap for project capital requirements + Max-Heap for affordable project profits.

### Logic / Approach
1. Sort projects by required capital.
2. Push all affordable projects (capital $\le W$) into Max-Heap.
3. Pop most profitable project, add profit to capital $W$, repeat $K$ times.

### Sample Input & Output
- **Input**: `k = 2, w = 0, profits = [1, 2, 3], capital = [0, 1, 1]`
- **Output**: `4`

### Explanation
1. Pick project 0 (capital 0, profit 1) $\rightarrow W = 1$.
2. Pick project 2 (capital 1, profit 3) $\rightarrow W = 4$.

### Python Implementation
- [`level_9_ipo_max_profit.py`](file:///c:/Users/chakr/Downloads/DSA/13-heap/level_9_ipo_max_profit.py)
