# Topic 10: Binary Search (Level 1 to Level 9)

Binary search is an $O(\log N)$ search algorithm that works by repeatedly dividing the search interval in half on sorted or monotonic search spaces.

---

## Level-1: Binary Search Basics

### Question
Given a sorted integer array `nums` and a `target`, return the index of `target` or `-1` if not found.

### Description / Explanation
Standard binary search implementation using left and right pointers.

### Logic / Approach
1. Set `left = 0`, `right = len(nums) - 1`.
2. Compute `mid = (left + right) // 2`.
3. Adjust boundaries depending on `nums[mid]` vs `target`.

### Sample Input & Output
- **Input**: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`
- **Output**: `4`

### Explanation
`nums[4] == 9`.

### Python Implementation
- [`level_1_binary_search_basics.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_1_binary_search_basics.py)

---

## Level-2: Search in Rotated Sorted Array

### Question
Search for `target` in a sorted array that has been rotated at an unknown pivot point.

### Description / Explanation
At least one half of the array (left or right of `mid`) is always strictly sorted.

### Logic / Approach
Determine which half is sorted, check if target falls in sorted range, and halve search window accordingly.

### Sample Input & Output
- **Input**: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`
- **Output**: `4`

### Explanation
Target `0` is at index `4`.

### Python Implementation
- [`level_2_search_rotated_array.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_2_search_rotated_array.py)

---

## Level-3: Find First and Last Position of Element

### Question
Find the starting and ending index of a target value in a sorted array.

### Description / Explanation
Run two modified binary searches to locate lower bound and upper bound.

### Logic / Approach
- For first position: when `nums[mid] == target`, save `mid` and continue search left (`right = mid - 1`).
- For last position: when `nums[mid] == target`, save `mid` and continue search right (`left = mid + 1`).

### Sample Input & Output
- **Input**: `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`
- **Output**: `[3, 4]`

### Explanation
First `8` is at index 3, last `8` is at index 4.

### Python Implementation
- [`level_3_first_last_position.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_3_first_last_position.py)

---

## Level-4: Search a 2D Matrix

### Question
Search for `target` in an $M \times N$ matrix where rows are sorted and first element of each row is greater than last element of previous row.

### Description / Explanation
Treat the 2D matrix as a flattened 1D sorted array of length $M \times N$.

### Logic / Approach
Map 1D index `mid` to 2D indices: `r = mid // N`, `c = mid % N`.

### Sample Input & Output
- **Input**: `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]`, `target = 3`
- **Output**: `True`

### Explanation
Element `3` exists at `matrix[0][1]`.

### Python Implementation
- [`level_4_search_2d_matrix.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_4_search_2d_matrix.py)

---

## Level-5: Find Peak Element

### Question
Find an element index that is strictly greater than its neighbors.

### Description / Explanation
Array can be viewed as climbing upward or downward.

### Logic / Approach
If `nums[mid] > nums[mid+1]`, peak lies on left half including `mid`. Otherwise, peak lies on right half.

### Sample Input & Output
- **Input**: `nums = [1, 2, 3, 1]`
- **Output**: `2`

### Explanation
Element 3 at index 2 is greater than neighbors 2 and 1.

### Python Implementation
- [`level_5_find_peak_element.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_5_find_peak_element.py)

---

## Level-6: Koko Eating Bananas

### Question
Find minimum eating speed $K$ to finish all banana piles within $H$ hours.

### Description / Explanation
Binary search on the search space of speed $K \in [1, \max(piles)]$.

### Logic / Approach
Helper function `can_eat_all(speed)` calculates total hours. Binary search finds smallest valid speed.

### Sample Input & Output
- **Input**: `piles = [3, 6, 7, 11]`, `h = 8`
- **Output**: `4`

### Explanation
At speed 4, hours required $= 1 + 2 + 2 + 3 = 8 \le 8$.

### Python Implementation
- [`level_6_koko_eating_bananas.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_6_koko_eating_bananas.py)

---

## Level-7: Capacity To Ship Packages Within D Days

### Question
Find minimum ship capacity required to ship all packages in `days`.

### Description / Explanation
Binary search on answer capacity range $[\max(weights), \sum(weights)]$.

### Logic / Approach
Check if capacity can fit packages within $D$ days.

### Sample Input & Output
- **Input**: `weights = [1,2,3,4,5,6,7,8,9,10]`, `days = 5`
- **Output**: `15`

### Explanation
1st day: 1..5 (15), 2nd day: 6,7 (13), 3rd day: 8 (8), 4th day: 9 (9), 5th day: 10 (10).

### Python Implementation
- [`level_7_ship_capacity.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_7_ship_capacity.py)

---

## Level-8: Median of Two Sorted Arrays

### Question
Find the median of two sorted arrays `nums1` and `nums2` in $O(\log(\min(M,N)))$ time.

### Description / Explanation
Binary search on partition point of the smaller array.

### Logic / Approach
Partition both arrays such that left half elements $\le$ right half elements.

### Sample Input & Output
- **Input**: `nums1 = [1, 3]`, `nums2 = [2]`
- **Output**: `2.0`

### Explanation
Merged array $= [1, 2, 3]$, median $= 2.0$.

### Python Implementation
- [`level_8_median_two_sorted_arrays.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_8_median_two_sorted_arrays.py)

---

## Level-9: Split Array Largest Sum

### Question
Split `nums` into $K$ non-empty subarrays such that largest sum of any subarray is minimized.

### Description / Explanation
Binary search on minimum max-subarray-sum in range $[\max(nums), \sum(nums)]$.

### Logic / Approach
For candidate sum `mid`, greedily check how many subarrays are formed.

### Sample Input & Output
- **Input**: `nums = [7,2,5,10,8]`, `k = 2`
- **Output**: `18`

### Explanation
Subarrays `[7, 2, 5]` (sum 14) and `[10, 8]` (sum 18). Minimized max sum $= 18$.

### Python Implementation
- [`level_9_split_array_largest_sum.py`](file:///c:/Users/chakr/Downloads/DSA/10-binary-search/level_9_split_array_largest_sum.py)
