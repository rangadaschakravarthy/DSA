# 01-Arrays Module Curriculum & Problem Guide

---

## Level-1: Basic Array Traversal & Manipulation

### Problem 1: In-Place Array Reversal & Right Rotation
- **Question**: Given an array `nums` and an integer `k`, rotate the array to the right by `k` steps in-place.
- **Description / Explanation**: We need to shift elements to the right by `k` positions without using extra array memory.
- **Approach & Logic**:
  1. Reverse the entire array.
  2. Reverse the first `k` elements.
  3. Reverse the remaining `n - k` elements.
- **Sample Input**: `nums = [1, 2, 3, 4, 5, 6, 7], k = 3`
- **Sample Output**: `[5, 6, 7, 1, 2, 3, 4]`
- **Explanation**: 
  - Entire reverse: `[7, 6, 5, 4, 3, 2, 1]`.
  - Reverse first 3: `[5, 6, 7, 4, 3, 2, 1]`.
  - Reverse last 4: `[5, 6, 7, 1, 2, 3, 4]`.
- **Python Implementation**: [`level_1_array_basics.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_1_array_basics.py)

---

## Level-2: Prefix Sum Arrays

### Problem 1: Range Sum Query O(1)
- **Question**: Given an integer array `nums`, process queries to calculate the sum of elements between indices `left` and `right` inclusive.
- **Description / Explanation**: Answer range sum queries in $O(1)$ time after $O(N)$ preprocessing.
- **Approach & Logic**:
  - Build prefix sum array `prefix[i] = prefix[i-1] + nums[i-1]` of length $N+1$.
  - Range sum: `query(left, right) = prefix[right + 1] - prefix[left]`.
- **Sample Input**: `nums = [-2, 0, 3, -5, 2, -1], left = 0, right = 2`
- **Sample Output**: `1`
- **Explanation**: Sum of `nums[0] + nums[1] + nums[2] = (-2) + 0 + 3 = 1`.
- **Python Implementation**: [`level_2_prefix_sum.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_2_prefix_sum.py)

---

## Level-3: Two Pointers Pattern

### Problem 1: Container With Most Water
- **Question**: Given `n` non-negative integers representing vertical lines, find two lines that together with the x-axis form a container holding the most water.
- **Description / Explanation**: Maximize $\text{area} = \min(h[l], h[r]) \times (r - l)$.
- **Approach & Logic**:
  - Two Pointers starting at opposite ends: `left = 0`, `right = n - 1`.
  - Calculate area, update `max_water`.
  - Move the pointer pointing to the shorter vertical line inwards.
- **Sample Input**: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- **Sample Output**: `49`
- **Explanation**: Lines at index 1 ($h=8$) and index 8 ($h=7$) form container of width $7$ and height $\min(8, 7) = 7$. Area $= 7 \times 7 = 49$.
- **Python Implementation**: [`level_3_two_pointers.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_3_two_pointers.py)

---

## Level-4: Kadane's Algorithm

### Problem 1: Maximum Subarray Sum
- **Question**: Find the contiguous subarray within a 1D array of numbers which has the largest sum.
- **Description / Explanation**: Optimize $O(N^2)$ brute force to $O(N)$ single pass using dynamic programming / Kadane's.
- **Approach & Logic**:
  - Maintain `current_max = max(nums[i], current_max + nums[i])`.
  - Global `max_so_far = max(max_so_far, current_max)`.
- **Sample Input**: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- **Sample Output**: `6`
- **Explanation**: Continuous subarray `[4, -1, 2, 1]` has maximum sum $= 6$.
- **Python Implementation**: [`level_4_kadane.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_4_kadane.py)

---

## Level-5: Dutch National Flag Algorithm

### Problem 1: Sort Colors (0s, 1s, 2s)
- **Question**: Sort an array containing only 0s, 1s, and 2s in-place in a single pass.
- **Description / Explanation**: Partition array into 3 sections using 3 pointers in $O(N)$ time and $O(1)$ extra space.
- **Approach & Logic**:
  - Pointers: `low = 0`, `mid = 0`, `high = n - 1`.
  - If `nums[mid] == 0`: swap `nums[low]` and `nums[mid]`, `low++`, `mid++`.
  - If `nums[mid] == 1`: `mid++`.
  - If `nums[mid] == 2`: swap `nums[mid]` and `nums[high]`, `high--`.
- **Sample Input**: `nums = [2, 0, 2, 1, 1, 0]`
- **Sample Output**: `[0, 0, 1, 1, 2, 2]`
- **Explanation**: Sorted in-place in 1 pass.
- **Python Implementation**: [`level_5_dutch_flag.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_5_dutch_flag.py)

---

## Level-6: 2D Matrix Manipulations

### Problem 1: Rotate Matrix 90 Degrees Clockwise
- **Question**: Rotate an $N \times N$ 2D matrix 90 degrees clockwise in-place.
- **Description / Explanation**: Transform rows to columns without extra matrix allocation.
- **Approach & Logic**:
  - Step 1: Transpose matrix in-place (`matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`).
  - Step 2: Reverse each row (`matrix[i].reverse()`).
- **Sample Input**: 
  ```python
  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]
  ```
- **Sample Output**:
  ```python
  [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]
  ]
  ```
- **Explanation**: Transposed: `[[1,4,7],[2,5,8],[3,6,9]]`. Reversed rows: `[[7,4,1],[8,5,2],[9,6,3]]`.
- **Python Implementation**: [`level_6_matrix_2d.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_6_matrix_2d.py)

---

## Level-7: Sweep-Line & Interval Overlaps

### Problem 1: Meeting Rooms II
- **Question**: Given an array of meeting time intervals `[start, end]`, find the minimum number of conference rooms required.
- **Description / Explanation**: Track concurrent active meeting overlaps using Sweep-Line sorting.
- **Approach & Logic**:
  - Separate and sort `start` times and `end` times independently.
  - Iterate with two pointers `start_ptr` and `end_ptr`:
    - If `start[start_ptr] < end[end_ptr]`: room needed (`rooms++`, `start_ptr++`).
    - Else: meeting ended (`rooms--`, `end_ptr++`).
- **Sample Input**: `intervals = [[0, 30], [5, 10], [15, 20]]`
- **Sample Output**: `2`
- **Explanation**: At $t=5$, meeting 1 ($0-30$) and meeting 2 ($5-10$) overlap, requiring 2 rooms.
- **Python Implementation**: [`level_7_merge_intervals_array.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_7_merge_intervals_array.py)

---

## Level-8: Next Permutation

### Problem 1: Next Permutation In-Place
- **Question**: Rearrange numbers into the lexicographically next greater permutation in $O(N)$ time and $O(1)$ space.
- **Description / Explanation**: Find next permutation in dictionary order.
- **Approach & Logic**:
  1. Find rightmost pivot `i` where `nums[i] < nums[i+1]`.
  2. If no pivot, reverse array.
  3. Swap `nums[i]` with smallest element `nums[j] > nums[i]` to its right.
  4. Reverse suffix starting at `i+1`.
- **Sample Input**: `nums = [1, 2, 3]`
- **Sample Output**: `[1, 3, 2]`
- **Explanation**: Lexicographically next after `1, 2, 3` is `1, 3, 2`.
- **Python Implementation**: [`level_8_next_permutation.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_8_next_permutation.py)

---

## Level-9: Cyclic Sort Mastery

### Problem 1: First Missing Positive
- **Question**: Given an unsorted integer array `nums`, return the smallest missing positive integer in $O(N)$ time and $O(1)$ space.
- **Description / Explanation**: Place numbers in their correct 1-indexed position `nums[i] == i + 1`.
- **Approach & Logic**:
  - While `1 <= nums[i] <= N` and `nums[i] != nums[nums[i] - 1]`: swap `nums[i]` with `nums[nums[i] - 1]`.
  - Scan array: first index where `nums[idx] != idx + 1` gives answer `idx + 1`.
- **Sample Input**: `nums = [3, 4, -1, 1]`
- **Sample Output**: `2`
- **Explanation**: Cyclic sort yields `[1, -1, 3, 4]`. Index 1 has `-1 != 2`, so missing is `2`.
- **Python Implementation**: [`level_9_cyclic_sort.py`](file:///c:/Users/chakr/Downloads/DSA/01-arrays/level_9_cyclic_sort.py)
