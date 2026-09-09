# 03-Hashing Module Curriculum & Problem Guide

---

## Level-1: Hash Map & Hash Set Foundations

### Problem 1: Two Sum (Unsorted Array)
- **Question**: Given an array of integers `nums` and a target `target`, return indices of the two numbers such that they add up to `target`.
- **Description / Explanation**: Find pair in single pass $O(N)$ time using Hash Map lookup.
- **Approach & Logic**:
  - Hash map stores `seen[value] = index`.
  - For each `num`, check if `(target - num)` exists in `seen`.
- **Sample Input**: `nums = [2, 7, 11, 15], target = 9`
- **Sample Output**: `[0, 1]`
- **Explanation**: `nums[0] + nums[1] = 2 + 7 = 9`.
- **Python Implementation**: [`level_1_hashmap_basics.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_1_hashmap_basics.py)

---

## Level-2: Sequence Problems & Set Lookups

### Problem 1: Longest Consecutive Sequence
- **Question**: Find the length of the longest consecutive elements sequence in an unsorted array in $O(N)$ time.
- **Description / Explanation**: Find longest streak of integers `x, x+1, x+2...` without sorting.
- **Approach & Logic**:
  - Insert numbers into Hash Set.
  - Only start counting sequence if `(num - 1)` is NOT in set (ensures `num` is start of sequence).
- **Sample Input**: `nums = [100, 4, 200, 1, 3, 2]`
- **Sample Output**: `4`
- **Explanation**: Longest consecutive sequence is `[1, 2, 3, 4]` (length 4).
- **Python Implementation**: [`level_2_consecutive_sequence.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_2_consecutive_sequence.py)

---

## Level-3: Subarray Sum Remainder Maps

### Problem 1: Subarray Sums Divisible by K
- **Question**: Find total number of continuous subarrays whose sum is divisible by `k`.
- **Description / Explanation**: Use Prefix Sum Modular Remainder frequency hash map in $O(N)$ time.
- **Approach & Logic**:
  - If `prefix_sum[j] % k == prefix_sum[i] % k`, then sum of subarray `nums[i+1...j]` is divisible by `k`.
  - Maintain frequency dictionary of remainders.
- **Sample Input**: `nums = [4, 5, 0, -2, -3, 1], k = 5`
- **Sample Output**: `7`
- **Explanation**: 7 valid subarrays sum to multiples of 5.
- **Python Implementation**: [`level_3_subarray_divisible.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_3_subarray_divisible.py)

---

## Level-4: Prefix Sum & Product Window Maps

### Problem 1: Subarray Sum Equals K
- **Question**: Return total number of continuous subarrays whose sum equals `k`.
- **Description / Explanation**: Match prefix sum difference `current_sum - k` in hash map.
- **Approach & Logic**:
  - `prefix_counts[0] = 1`. Update `count += prefix_counts[current_sum - k]`.
- **Sample Input**: `nums = [1, 1, 1], k = 2`
- **Sample Output**: `2`
- **Explanation**: Subarrays `[1, 1]` at index 0-1 and index 1-2 both sum to 2.
- **Python Implementation**: [`level_4_prefix_sum_hashmap.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_4_prefix_sum_hashmap.py)

---

## Level-5: Custom HashMap Design

### Problem 1: Design HashMap (Chaining Method)
- **Question**: Design a HashMap without using built-in hash table libraries supporting `put`, `get`, `remove` in $O(1)$ average time.
- **Description / Explanation**: Construct bucket array with separate chaining linked lists for collision resolution.
- **Approach & Logic**:
  - Array of 1000 buckets. Index: `key % 1000`.
  - Store key-value tuples in bucket list.
- **Sample Input**: `put(1, 1), put(2, 2), get(1), get(3), put(2, 1), remove(2)`
- **Sample Output**: `get(1) -> 1, get(3) -> -1, get(2) -> -1`
- **Explanation**: Operations execute in $O(1)$ average time.
- **Python Implementation**: [`level_5_custom_hashmap.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_5_custom_hashmap.py)

---

## Level-6: Frequency Window Search

### Problem 1: Minimum Window Substring
- **Question**: Find smallest window in `s` containing all characters of `t` in $O(N)$ time.
- **Description / Explanation**: Sliding window with character frequency count map.
- **Approach & Logic**:
  - Expand `right` until all required characters matched.
  - Shrink `left` to find minimal valid length window.
- **Sample Input**: `s = "ADOBECODEBANC", t = "ABC"`
- **Sample Output**: `"BANC"`
- **Explanation**: `"BANC"` is shortest window containing 'A', 'B', and 'C'.
- **Python Implementation**: [`level_6_frequency_window_hash.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_6_frequency_window_hash.py)

---

## Level-7: LRU Cache Design

### Problem 1: Least Recently Used (LRU) Cache
- **Question**: Design LRU Cache data structure supporting `get(key)` and `put(key, value)` in $O(1)$ time.
- **Description / Explanation**: Evict least recently accessed item when capacity reached.
- **Approach & Logic**:
  - Hash Map (key -> Node) + Doubly Linked List (Head = MRU, Tail = LRU).
- **Sample Input**: `LRUCache(2), put(1,1), put(2,2), get(1), put(3,3), get(2)`
- **Sample Output**: `get(1) -> 1, get(2) -> -1`
- **Explanation**: `put(3,3)` evicts key 2 because key 1 was recently accessed.
- **Python Implementation**: [`level_7_lru_cache.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_7_lru_cache.py)

---

## Level-8: LFU Cache Design

### Problem 1: Least Frequently Used (LFU) Cache
- **Question**: Design LFU Cache data structure supporting `get` and `put` in $O(1)$ time.
- **Description / Explanation**: Evict least frequently used item. Tie-breaker: least recently used.
- **Approach & Logic**:
  - `key_map` (key -> Node) + `freq_map` (frequency -> DoublyLinkedList) + `min_freq` tracker.
- **Sample Input**: `LFUCache(2), put(1,1), put(2,2), get(1), put(3,3), get(2)`
- **Sample Output**: `get(1) -> 1, get(2) -> -1, get(3) -> 3`
- **Explanation**: `put(3,3)` evicts key 2 (frequency 1 vs key 1 frequency 2).
- **Python Implementation**: [`level_8_lfu_cache.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_8_lfu_cache.py)

---

## Level-9: Consistent Hashing Ring

### Problem 1: Consistent Hashing Ring with Virtual Nodes
- **Question**: Design a Consistent Hashing Ring for distributed hash table key partitioning across physical servers.
- **Description / Explanation**: Minimize key remapping when servers are added or removed.
- **Approach & Logic**:
  - Hash ring $[0, 2^{32}-1]$. Map $K$ virtual nodes per server onto ring using MD5 hash.
  - Binary search (`bisect_right`) to route keys to nearest server clockwise.
- **Sample Input**: `add_node("Server-A"), add_node("Server-B"), get_node("user_1001")`
- **Sample Output**: `"Server-A"` (or `"Server-B"`)
- **Explanation**: Key routed consistently to server's virtual node on hash ring.
- **Python Implementation**: [`level_9_consistent_hashing.py`](file:///c:/Users/chakr/Downloads/DSA/03-hashing/level_9_consistent_hashing.py)
