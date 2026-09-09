# 07-Queue Module Curriculum & Problem Guide

---

## Level-1: Queue Fundamentals & Two-Stack Queue Design

### Problem 1: Implement Queue using Stacks
- **Question**: Implement a First-In-First-Out (FIFO) queue using only two standard LIFO stacks.
- **Description / Explanation**: Support `push`, `pop`, `peek`, and `empty` with $O(1)$ amortized time.
- **Approach & Logic**:
  - `in_stack` for enqueueing (`push`). `out_stack` for dequeueing (`pop`/`peek`).
  - Transfer elements from `in_stack` to `out_stack` when `out_stack` is empty.
- **Sample Input**: `push(1), push(2), peek(), pop(), empty()`
- **Sample Output**: `peek() -> 1, pop() -> 1, empty() -> False`
- **Explanation**: First element pushed (1) is first element returned.
- **Python Implementation**: [`level_1_queue_stack.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_1_queue_stack.py)

---

## Level-2: Monotonic Deque & Sliding Window Maximum

### Problem 1: Sliding Window Maximum
- **Question**: Return the max sliding window values in $O(N)$ time.
- **Description / Explanation**: Use Monotonic Decreasing Deque to track window maximum.
- **Approach & Logic**:
  - Maintain deque of indices in strictly decreasing order of values.
  - Remove indices outside window `index <= i - k`. Max is `nums[deque[0]]`.
- **Sample Input**: `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`
- **Sample Output**: `[3, 3, 5, 5, 6, 7]`
- **Explanation**: Max values for sliding windows of size 3.
- **Python Implementation**: [`level_2_sliding_window_max.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_2_sliding_window_max.py)

---

## Level-3: Array-Based Circular Queue Design

### Problem 1: Design Circular Queue
- **Question**: Design a Ring Buffer / Circular Queue supporting `enQueue`, `deQueue`, `Front`, `Rear` in $O(1)$ time.
- **Description / Explanation**: Reuse array slots in circular fashion using modulo arithmetic.
- **Approach & Logic**:
  - Fixed capacity `k`, `head` pointer, and `count` tracker.
  - `tail = (head + count) % capacity`.
- **Sample Input**: `MyCircularQueue(3), enQueue(1), enQueue(2), enQueue(3), enQueue(4), Rear()`
- **Sample Output**: `enQueue(4) -> False, Rear() -> 3`
- **Explanation**: Enqueuing 4 fails because capacity 3 is reached. Rear is 3.
- **Python Implementation**: [`level_3_circular_queue.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_3_circular_queue.py)

---

## Level-4: Sliding Window Stream Moving Average

### Problem 1: Moving Average from Data Stream
- **Question**: Calculate moving average of a stream of integers within a sliding window of fixed size in $O(1)$ time.
- **Description / Explanation**: Sliding window queue tracking running sum.
- **Approach & Logic**:
  - Maintain running `sum`. When queue length reaches `size`, subtract `queue.popleft()`.
- **Sample Input**: `MovingAverage(3), next(1), next(10), next(3), next(5)`
- **Sample Output**: `next(1) -> 1.0, next(10) -> 5.5, next(3) -> 4.66667, next(5) -> 6.0`
- **Explanation**: Window `[10, 3, 5]` has sum $18 / 3 = 6.0$.
- **Python Implementation**: [`level_4_moving_average.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_4_moving_average.py)

---

## Level-5: Time-Window Call Counter Queue

### Problem 1: Number of Recent Calls
- **Question**: Count number of recent requests within time frame $[t - 3000, t]$ in $O(1)$ amortized time.
- **Description / Explanation**: Queue tracking timestamps in sliding window of 3000ms.
- **Approach & Logic**:
  - Enqueue `t`. While `queue[0] < t - 3000`: `queue.popleft()`. Return `len(queue)`.
- **Sample Input**: `ping(1), ping(100), ping(3001), ping(3002)`
- **Sample Output**: `1, 2, 3, 3`
- **Explanation**: `ping(3002)` pops timestamp 1 (outside range $[2, 3002]$). Count remains 3.
- **Python Implementation**: [`level_5_recent_calls.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_5_recent_calls.py)

---

## Level-6: First Unique Stream Queue & Frequency Map

### Problem 1: First Unique Number in a Stream
- **Question**: Return first non-repeating number in a data stream in $O(1)$ amortized time.
- **Description / Explanation**: Combine FIFO Queue with character frequency dictionary.
- **Approach & Logic**:
  - Enqueue incoming values and update frequency map.
  - On `showFirstUnique()`: pop elements from queue front while `counts[queue[0]] > 1`.
- **Sample Input**: `FirstUnique([2, 3, 5]), showFirstUnique(), add(2), showFirstUnique()`
- **Sample Output**: `2, 3`
- **Explanation**: After adding 2, 2 is repeated so first unique becomes 3.
- **Python Implementation**: [`level_6_first_unique_stream.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_6_first_unique_stream.py)

---

## Level-7: Task Scheduler Queue & Priority Queue Cooling

### Problem 1: Task Scheduler
- **Question**: Find minimum CPU intervals needed to execute all tasks with cooling period `n` in $O(N)$ time.
- **Description / Explanation**: Max-Heap for task selection + Queue for cooling down tasks.
- **Approach & Logic**:
  - Max-Heap stores task counts. Deque stores cooling tasks `(count, available_time)`.
  - Process unit time by unit time. Push cooled tasks back to Max-Heap when `time == available_time`.
- **Sample Input**: `tasks = ["A","A","A","B","B","B"], n = 2`
- **Sample Output**: `8`
- **Explanation**: Execution order: `A -> B -> idle -> A -> B -> idle -> A -> B` (8 intervals).
- **Python Implementation**: [`level_7_task_scheduler.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_7_task_scheduler.py)

---

## Level-8: Monotonic Deque & Prefix Sum Optimization

### Problem 1: Shortest Subarray with Sum at Least K
- **Question**: Return length of shortest non-empty continuous subarray with sum at least `k` in $O(N)$ time.
- **Description / Explanation**: Prefix sum array + Monotonic Increasing Deque.
- **Approach & Logic**:
  - Prefix sum `prefix[i]`. Maintain Monotonic Increasing Deque of indices.
  - While `prefix[i] - prefix[q[0]] >= k`: shrink `min_len = min(min_len, i - q.popleft())`.
- **Sample Input**: `nums = [2, -1, 2], k = 3`
- **Sample Output**: `3`
- **Explanation**: Entire array `[2, -1, 2]` sums to $3 \ge 3$ (length 3).
- **Python Implementation**: [`level_8_shortest_subarray_sum_k.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_8_shortest_subarray_sum_k.py)

---

## Level-9: DP + Monotonic Deque Optimization

### Problem 1: Constrained Subsequence Sum
- **Question**: Find maximum sum of a non-empty subsequence such that index distance $|i - j| \le k$ for consecutive elements in $O(N)$ time.
- **Description / Explanation**: Sliding window DP max optimization using Monotonic Decreasing Deque.
- **Approach & Logic**:
  - `dp[i] = nums[i] + max(0, max_{i-k <= j < i} dp[j])`.
  - Monotonic Decreasing Deque tracks max `dp[j]` in window of size `k`.
- **Sample Input**: `nums = [10, 2, -10, 5, 20], k = 2`
- **Sample Output**: `37`
- **Explanation**: Subsequence `[10, 2, 5, 20]` has max sum $= 10 + 2 + 5 + 20 = 37$.
- **Python Implementation**: [`level_9_max_constrained_subsequence.py`](file:///c:/Users/chakr/Downloads/DSA/07-queue/level_9_max_constrained_subsequence.py)
