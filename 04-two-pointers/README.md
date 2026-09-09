# 04-Two-Pointers Module Curriculum & Problem Guide

---

## Level-1: Fast & Slow Pointers (Floyd's Cycle Finding)

### Problem 1: Find the Duplicate Number
- **Question**: Given an array of integers `nums` containing $N + 1$ integers where each integer is in range $[1, N]$, find the duplicate number without modifying array in $O(N)$ time and $O(1)$ space.
- **Description / Explanation**: Treat array values as pointers `nums[i] -> nums[nums[i]]`. The duplicate number is the entry point of the cycle.
- **Approach & Logic**:
  - Phase 1: Advance `slow = nums[slow]` and `fast = nums[nums[fast]]` until collision.
  - Phase 2: Reset `slow = nums[0]`, advance both by 1 step until they meet at cycle entrance.
- **Sample Input**: `nums = [1, 3, 4, 2, 2]`
- **Sample Output**: `2`
- **Explanation**: Cycle entrance node is 2.
- **Python Implementation**: [`level_1_fast_slow.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_1_fast_slow.py)

---

## Level-2: Boundary Two Pointers Optimization

### Problem 1: Trapping Rain Water
- **Question**: Given $N$ non-negative integers representing elevation map, compute total trapped water after raining in $O(N)$ time and $O(1)$ space.
- **Description / Explanation**: Water trapped above bar $i$ is $\min(\text{left\_max}, \text{right\_max}) - \text{height}[i]$.
- **Approach & Logic**:
  - Two pointers `left = 0`, `right = n - 1` with `left_max` and `right_max`.
  - Advance the pointer with smaller boundary max.
- **Sample Input**: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
- **Sample Output**: `6`
- **Explanation**: Total 6 units of water trapped.
- **Python Implementation**: [`level_2_trapping_rain_water.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_2_trapping_rain_water.py)

---

## Level-3: Triplet Target Search (3Sum)

### Problem 1: 3Sum Triplet Search
- **Question**: Find all unique triplets `[nums[i], nums[j], nums[k]]` such that `nums[i] + nums[j] + nums[k] == 0`.
- **Description / Explanation**: Eliminate duplicate triplets and find zero-sum pairs in $O(N^2)$ time.
- **Approach & Logic**:
  - Sort array. Loop `i` from `0` to `n-3`.
  - Use opposite two pointers `left = i + 1`, `right = n - 1` to find two sum target `-nums[i]`. Skip duplicate values.
- **Sample Input**: `nums = [-1, 0, 1, 2, -1, -4]`
- **Sample Output**: `[[-1, -1, 2], [-1, 0, 1]]`
- **Explanation**: `(-1) + (-1) + 2 = 0` and `(-1) + 0 + 1 = 0`.
- **Python Implementation**: [`level_3_three_sum.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_3_three_sum.py)

---

## Level-4: Multi-Pointer Quadruplets (4Sum)

### Problem 1: 4Sum Quadruplet Search
- **Question**: Find all unique quadruplets `[a, b, c, d]` such that `a + b + c + d == target`.
- **Description / Explanation**: Extend 3Sum with an additional outer loop in $O(N^3)$ time and $O(1)$ space.
- **Approach & Logic**:
  - Double loop for first two numbers `a` and `b`.
  - Two pointers `left` and `right` for remaining sum `target - nums[a] - nums[b]`. Skip duplicate elements.
- **Sample Input**: `nums = [1, 0, -1, 0, -2, 2], target = 0`
- **Sample Output**: `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`
- **Explanation**: Unique quadruplets summing to 0.
- **Python Implementation**: [`level_4_four_sum.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_4_four_sum.py)

---

## Level-5: In-Place Array Partitioning

### Problem 1: Move Zeroes & Sort by Parity
- **Question**: Move all 0s to the end of the array while maintaining relative order of non-zero elements in-place.
- **Description / Explanation**: Partition array using Read and Write Pointers in $O(N)$ time and $O(1)$ space.
- **Approach & Logic**:
  - `write_idx = 0`. Whenever `nums[read_idx] != 0`, swap `nums[write_idx]` and `nums[read_idx]`, `write_idx++`.
- **Sample Input**: `nums = [0, 1, 0, 3, 12]`
- **Sample Output**: `[1, 3, 12, 0, 0]`
- **Explanation**: Non-zeros moved to front preserving relative order; zeroes pushed to end.
- **Python Implementation**: [`level_5_partition_array.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_5_partition_array.py)

---

## Level-6: Subarray Range Two-Pointer Bounds

### Problem 1: Shortest Unsorted Continuous Subarray
- **Question**: Find length of shortest subarray that, if sorted, makes the entire array sorted in $O(N)$ time and $O(1)$ space.
- **Description / Explanation**: Track out-of-order element bounds from both ends.
- **Approach & Logic**:
  - Left-to-right pass: find rightmost index smaller than `max_seen`.
  - Right-to-left pass: find leftmost index larger than `min_seen`.
- **Sample Input**: `nums = [2, 6, 4, 8, 10, 9, 15]`
- **Sample Output**: `5`
- **Explanation**: Subarray `[6, 4, 8, 10, 9]` (length 5) must be sorted.
- **Python Implementation**: [`level_6_shortest_unsorted.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_6_shortest_unsorted.py)

---

## Level-7: Two Pointers Branching

### Problem 1: Valid Palindrome II
- **Question**: Check if string `s` can become a palindrome after deleting at most one character in $O(N)$ time and $O(1)$ space.
- **Description / Explanation**: Handle single character deletion mismatch with two-pointer branching.
- **Approach & Logic**:
  - On mismatch `s[left] != s[right]`: return True if `s[left+1..right]` IS palindrome OR `s[left..right-1]` IS palindrome.
- **Sample Input**: `s = "abca"`
- **Sample Output**: `True`
- **Explanation**: Deleting `'c'` leaves `"aba"` which is a valid palindrome.
- **Python Implementation**: [`level_7_palindrome_ii.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_7_palindrome_ii.py)

---

## Level-8: Greedy Two Pointers & Capacity Limits

### Problem 1: Boats to Save People
- **Question**: Find minimum number of boats needed to carry all people given max weight capacity `limit` (max 2 people/boat) in $O(N \log N)$ time.
- **Description / Explanation**: Pair heaviest person with lightest person greedily.
- **Approach & Logic**:
  - Sort weights. `left = 0`, `right = n - 1`.
  - If `people[left] + people[right] <= limit`: `left++`. Always decrement `right--` and increment `boats++`.
- **Sample Input**: `people = [3, 2, 2, 1], limit = 3`
- **Sample Output**: `3`
- **Explanation**: Boats: `(1, 2)`, `(2)`, `(3)`. Min boats = 3.
- **Python Implementation**: [`level_8_boats_save_people.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_8_boats_save_people.py)

---

## Level-9: Hybrid Two-Pointer Monotonic Deque

### Problem 1: Longest Subarray With Absolute Diff <= Limit
- **Question**: Find length of longest continuous subarray such that absolute diff between any two elements $\le \text{limit}$ in $O(N)$ time.
- **Description / Explanation**: Maintain sliding window range using two monotonic deques for window max and min.
- **Approach & Logic**:
  - `max_q` tracks window max; `min_q` tracks window min.
  - Advance `right`. While `max_q[0] - min_q[0] > limit`: advance `left` and pop out-of-bounds indices.
- **Sample Input**: `nums = [8, 2, 4, 7], limit = 4`
- **Sample Output**: `2`
- **Explanation**: Longest valid subarray is `[2, 4]` (diff $|4-2| = 2 \le 4$).
- **Python Implementation**: [`level_9_bounded_diff_subarray.py`](file:///c:/Users/chakr/Downloads/DSA/04-two-pointers/level_9_bounded_diff_subarray.py)
