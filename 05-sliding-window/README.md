# 05-Sliding-Window Module Curriculum & Problem Guide

---

## Level-1: Fixed & Semi-Fixed Sliding Window

### Problem 1: Maximum Sum Subarray of Size K
- **Question**: Given an array of integers `arr` and a number `k`, find the maximum sum of any contiguous subarray of size `k`.
- **Description / Explanation**: Slide window of fixed width `k` in $O(N)$ time.
- **Approach & Logic**:
  - `window_sum = sum(arr[:k])`.
  - For `i` from `k` to `n-1`: `window_sum += arr[i] - arr[i - k]`.
- **Sample Input**: `arr = [2, 1, 5, 1, 3, 2], k = 3`
- **Sample Output**: `9`
- **Explanation**: Subarray `[5, 1, 3]` has max sum $= 5 + 1 + 3 = 9$.
- **Python Implementation**: [`level_1_fixed_window.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_1_fixed_window.py)

---

## Level-2: Variable Window & At-Most-K Pattern

### Problem 1: Subarrays with K Different Integers
- **Question**: Given an integer array `nums` and an integer `k`, return the number of good subarrays (subarrays with exactly `k` different integers).
- **Description / Explanation**: Compute exact $K$ count using formula: $\text{Exact}(K) = \text{AtMost}(K) - \text{AtMost}(K - 1)$.
- **Approach & Logic**:
  - `at_most_k(k)` expands `right` pointer, shrinks `left` pointer when distinct count $> k$.
- **Sample Input**: `nums = [1, 2, 1, 2, 3], k = 2`
- **Sample Output**: `7`
- **Explanation**: 7 continuous subarrays contain exactly 2 distinct integers.
- **Python Implementation**: [`level_2_variable_at_most_k.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_2_variable_at_most_k.py)

---

## Level-3: Longest Substring with At Most K Distinct Characters

### Problem 1: Longest Substring K-Distinct
- **Question**: Find the length of the longest substring of `s` that contains at most `k` distinct characters.
- **Description / Explanation**: Variable window with character frequency map.
- **Approach & Logic**:
  - Expand `right`. While `len(counts) > k`: shrink `left` until distinct count $\le k$.
- **Sample Input**: `s = "eceba", k = 2`
- **Sample Output**: `3`
- **Explanation**: Longest valid substring is `"ece"` (length 3).
- **Python Implementation**: [`level_3_longest_substring_k_distinct.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_3_longest_substring_k_distinct.py)

---

## Level-4: Fruit Into Baskets

### Problem 1: Fruit Into Baskets (At Most 2 Types)
- **Question**: Find maximum number of fruits you can collect in 2 baskets (at most 2 distinct fruit types).
- **Description / Explanation**: Sliding window maintaining `len(basket_map) <= 2`.
- **Approach & Logic**:
  - Expand `right`. Shrink `left` whenever basket contains $> 2$ types.
- **Sample Input**: `fruits = [1, 2, 3, 2, 2]`
- **Sample Output**: `4`
- **Explanation**: Subarray `[2, 3, 2, 2]` contains 2 fruit types (2 and 3) with max length 4.
- **Python Implementation**: [`level_4_fruit_into_baskets.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_4_fruit_into_baskets.py)

---

## Level-5: Permutation in String

### Problem 1: Fixed Frequency Window Matching
- **Question**: Check if `s2` contains a permutation of `s1`.
- **Description / Explanation**: Compare frequency arrays of length 26 in sliding window of size `len(s1)`.
- **Approach & Logic**:
  - Fixed window size `len(s1)`. Update frequency count: add entering char, subtract exiting char.
- **Sample Input**: `s1 = "ab", s2 = "eidbaooo"`
- **Sample Output**: `True`
- **Explanation**: Substring `"ba"` at index 3 is a permutation of `"ab"`.
- **Python Implementation**: [`level_5_permutation_in_string.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_5_permutation_in_string.py)

---

## Level-6: Max Consecutive Ones III

### Problem 1: Max Consecutive Ones with K Flips
- **Question**: Find maximum number of consecutive 1s if you can flip at most `k` 0s to 1s.
- **Description / Explanation**: Variable window maintaining `zero_count <= k`.
- **Approach & Logic**:
  - Expand `right`. Increment `zero_count` if `nums[right] == 0`. While `zero_count > k`: shrink `left`.
- **Sample Input**: `nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2`
- **Sample Output**: `6`
- **Explanation**: Flipping two 0s at index 3 and 4 gives consecutive 1s `[1, 1, 1, 1, 1, 1]` (length 6).
- **Python Implementation**: [`level_6_max_consecutive_ones.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_6_max_consecutive_ones.py)

---

## Level-7: Minimum Window Subsequence

### Problem 1: Minimum Window Subsequence
- **Question**: Find shortest substring of `s1` that contains `s2` as a subsequence in $O(N \cdot M)$ time.
- **Description / Explanation**: Forward pass to match `s2`, backward pass to shrink window to minimal start index.
- **Approach & Logic**:
  - Forward: match characters of `s2`. Once complete, shrink `p1` backwards to find exact minimum start index.
- **Sample Input**: `s1 = "abcdebdde", s2 = "bde"`
- **Sample Output**: `"bcde"`
- **Explanation**: `"bcde"` is shorter than `"bdde"` and contains `"bde"` as a subsequence.
- **Python Implementation**: [`level_7_min_window_subsequence.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_7_min_window_subsequence.py)

---

## Level-8: Substring with Concatenation of All Words

### Problem 1: Substring Concatenation Search
- **Question**: Find all starting indices of substring(s) in `s` that is a concatenation of each word in `words` exactly once.
- **Description / Explanation**: Slide window in word-length increments.
- **Approach & Logic**:
  - Iterate `i` from `0` to `word_len - 1`. Maintain word frequency window map.
- **Sample Input**: `s = "barfoothefoobarman", words = ["foo", "bar"]`
- **Sample Output**: `[0, 9]`
- **Explanation**: Substrings `"barfoo"` at index 0 and `"foobar"` at index 9 contain all words.
- **Python Implementation**: [`level_8_substring_concatenation_words.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_8_substring_concatenation_words.py)

---

## Level-9: Sliding Window Median

### Problem 1: Sliding Window Median
- **Question**: Find the median of each sliding window of size `k` moving from left to right in $O(N \log K)$ time.
- **Description / Explanation**: Maintain sorted array window using `bisect`.
- **Approach & Logic**:
  - `window = sorted(nums[:k])`.
  - For each step: calculate median, remove `nums[i - k]`, insert `nums[i]` using `bisect.insort`.
- **Sample Input**: `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`
- **Sample Output**: `[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]`
- **Explanation**: Medians of sliding windows: `[1, 3, -1]` -> 1.0, `[3, -1, -3]` -> -1.0, etc.
- **Python Implementation**: [`level_9_sliding_window_median.py`](file:///c:/Users/chakr/Downloads/DSA/05-sliding-window/level_9_sliding_window_median.py)
