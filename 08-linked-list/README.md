# Topic 8: Linked List (Level 1 to Level 9)

Welcome to the Linked List topic! Linked Lists are fundamental linear data structures where elements (nodes) are stored sequentially in memory via pointers. Mastery of linked lists requires strong pointer manipulation, dummy node strategies, and fast & slow pointer techniques.

---

## Level-1: Linked List Basics & Pointer Manipulation

### Question
Given the head of a singly linked list, perform basic operations: reverse the linked list in-place and find the middle node of the list.

### Description / Explanation
- **Reverse Linked List**: Change the direction of pointers so that the tail becomes the head and every `next` pointer points to the previous node.
- **Find Middle Node**: Use the two-pointer technique (fast and slow pointer) where fast moves 2 steps and slow moves 1 step. When fast reaches the end, slow is at the middle.

### Logic / Approach
1. **Reverse**: Maintain `prev = None`, `curr = head`. Loop through list: save `next_node = curr.next`, set `curr.next = prev`, shift `prev = curr` and `curr = next_node`.
2. **Middle Node**: Initialize `slow = head` and `fast = head`. Advance `slow = slow.next` and `fast = fast.next.next` until `fast` or `fast.next` is `None`. Return `slow`.

### Sample Input & Output
- **Input**: List `[1, 2, 3, 4, 5]`
- **Output**: 
  - Reversed: `[5, 4, 3, 2, 1]`
  - Middle Node Value: `3`

### Explanation
- For Reverse: `1 -> 2 -> 3 -> 4 -> 5` reversed becomes `5 -> 4 -> 3 -> 2 -> 1`.
- For Middle: List length is 5. Fast pointer moves 2 steps twice to reach 5. Slow moves 1 step twice to reach node 3.

### Python Implementation
- [`level_1_linked_list_basics.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_1_linked_list_basics.py)

---

## Level-2: Linked List Cycle Detection

### Question
Given the head of a linked list, determine if the linked list has a cycle in it. If there is a cycle, return the node where the cycle begins; otherwise, return `None`.

### Description / Explanation
A cycle exists in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

### Logic / Approach (Floyd's Cycle Finding Algorithm)
1. Initialize `slow = head` and `fast = head`.
2. Traverse: `slow = slow.next` (1 step), `fast = fast.next.next` (2 steps).
3. If `slow == fast`, a cycle is detected.
4. To find cycle start: Reset `slow = head`. Move both `slow` and `fast` 1 step at a time until they meet again. The meeting node is the cycle start.

### Sample Input & Output
- **Input**: Head of list `[3, 2, 0, -4]` with tail connecting to node at index 1 (`2`).
- **Output**: Cycle detected = `True`, Cycle Start Node Value = `2`

### Explanation
Fast and slow pointers enter the cycle and eventually meet at node `-4`. Resetting `slow` to head (`3`) and moving both 1 step results in meeting at node `2`.

### Python Implementation
- [`level_2_cycle_detection.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_2_cycle_detection.py)

---

## Level-3: Merge K Sorted Lists

### Question
You are given an array of $K$ linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

### Description / Explanation
Efficiently combine $K$ pre-sorted linked lists into a single consolidated sorted list.

### Logic / Approach
- **Min-Heap Approach**:
  1. Insert the head node of each non-empty list into a Min-Heap keyed by node value.
  2. Pop the smallest node from the heap, append it to the result linked list.
  3. If the popped node has a `.next` node, push `.next` into the heap.
  4. Repeat until heap is empty.
- **Complexity**: Time $O(N \log K)$, Space $O(K)$.

### Sample Input & Output
- **Input**: `lists = [[1, 4, 5], [1, 3, 4], [2, 6]]`
- **Output**: `[1, 1, 2, 3, 4, 4, 5, 6]`

### Explanation
Min-heap compares `[1, 1, 2]`. Pops `1`, inserts `4`. Pops `1`, inserts `3`. Builds total sorted order `1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`.

### Python Implementation
- [`level_3_merge_k_lists.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_3_merge_k_lists.py)

---

## Level-4: Reorder List

### Question
You are given the head of a singly linked-list `L0 -> L1 -> ... -> Ln-1 -> Ln`. Reorder the list to be of the form: `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`.

### Description / Explanation
Reorder list nodes in-place without modifying node values.

### Logic / Approach
1. Find middle of linked list using Fast & Slow pointers.
2. Split list into two halves and reverse the second half.
3. Interleave/merge the first half and reversed second half node by node.

### Sample Input & Output
- **Input**: `[1, 2, 3, 4, 5]`
- **Output**: `[1, 5, 2, 4, 3]`

### Explanation
- Middle split: `[1, 2, 3]` and `[4, 5]`.
- Reverse 2nd half: `[5, 4]`.
- Interleave: `1 -> 5 -> 2 -> 4 -> 3`.

### Python Implementation
- [`level_4_reorder_list.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_4_reorder_list.py)

---

## Level-5: Reverse Nodes in k-Group

### Question
Given the head of a linked list, reverse the nodes of a linked list $k$ at a time and return its modified list. If the number of nodes is not a multiple of $k$, left-out nodes at the end should remain as they are.

### Description / Explanation
Reversing linked list nodes in fixed segment blocks of length $k$.

### Logic / Approach
1. Count if at least $k$ nodes remain from current position.
2. If fewer than $k$ nodes remain, leave them untouched.
3. Otherwise, reverse $k$ nodes iteratively.
4. Recursively process remaining list and attach result to tail of reversed segment.

### Sample Input & Output
- **Input**: `head = [1, 2, 3, 4, 5], k = 2`
- **Output**: `[2, 1, 4, 3, 5]`

### Explanation
- Group 1 `[1, 2]` reversed to `[2, 1]`.
- Group 2 `[3, 4]` reversed to `[4, 3]`.
- Node `[5]` remains unchanged as remaining count < $k=2$.

### Python Implementation
- [`level_5_reverse_k_group.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_5_reverse_k_group.py)

---

## Level-6: Add Two Numbers

### Question
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order. Add the two numbers and return the sum as a linked list.

### Description / Explanation
Perform digit-by-digit addition with carry propagation from least significant digit to most significant digit.

### Logic / Approach
1. Maintain `dummy` head, `curr` pointer, and `carry = 0`.
2. Loop while `l1`, `l2`, or `carry` is non-zero.
3. `val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry`.
4. Update `carry = val // 10`, append `ListNode(val % 10)`.
5. Advance pointers.

### Sample Input & Output
- **Input**: `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]`
- **Output**: `[7, 0, 8]`

### Explanation
- $2 + 5 = 7$ (carry 0)
- $4 + 6 = 10 \rightarrow 0$ (carry 1)
- $3 + 4 + 1 = 8$ (carry 0)
- Representing $342 + 465 = 807$.

### Python Implementation
- [`level_6_add_two_numbers.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_6_add_two_numbers.py)

---

## Level-7: Flatten a Multilevel Doubly Linked List

### Question
Flatten a multilevel doubly linked list where nodes have `next`, `prev`, and `child` pointers so that all nodes appear in a single-level doubly linked list.

### Description / Explanation
Traverse list; whenever a `child` pointer is present, insert the flattened child list between the current node and its original `next` node.

### Logic / Approach
1. Iterate `curr` through list.
2. If `curr.child` exists:
   - Recursively flatten `curr.child`.
   - Connect `curr.next` to flattened child.
   - Find tail of child list and connect tail's `next` to original `curr.next`.
   - Set `curr.child = None`.
3. Advance `curr = curr.next`.

### Sample Input & Output
- **Input**: `1 <-> 2 <-> 3` with node `3` child pointing to `4 <-> 5`
- **Output**: `1 <-> 2 <-> 3 <-> 4 <-> 5`

### Explanation
Child list `[4, 5]` is inserted after node `3`.

### Python Implementation
- [`level_7_flatten_multilevel_list.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_7_flatten_multilevel_list.py)

---

## Level-8: LRU Cache

### Question
Design a Least Recently Used (LRU) Cache supporting `get(key)` and `put(key, value)` operations in $O(1)$ time complexity.

### Description / Explanation
Evicts the least recently accessed item when cache capacity is reached.

### Logic / Approach
- **Data Structure**: Hash Map (`key` $\rightarrow$ `DNode`) + Doubly Linked List (Dummy Head & Tail).
- `get`: If key in map, move corresponding node to Head (most recent) and return value.
- `put`: If key exists, update value and move node to Head. If new key and capacity full, remove node from Tail (least recent) and delete from map. Add new node to Head.

### Sample Input & Output
- **Input**: `cap = 2`, `put(1, 1)`, `put(2, 2)`, `get(1)`, `put(3, 3)`, `get(2)`
- **Output**: `get(1) = 1`, `get(2) = -1`

### Explanation
Accessing `1` makes `2` the LRU item. Adding `(3, 3)` evicts `2`. Calling `get(2)` returns `-1`.

### Python Implementation
- [`level_8_lru_cache.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_8_lru_cache.py)

---

## Level-9: LFU Cache

### Question
Design a Least Frequently Used (LFU) Cache supporting `get(key)` and `put(key, value)` in $O(1)$ time complexity. If frequency ties, evict least recently used item among them.

### Description / Explanation
Evicts item with smallest access frequency.

### Logic / Approach
- **Data Structures**:
  - `key_map`: `key` $\rightarrow$ `Node(key, val, freq)`
  - `freq_map`: `freq` $\rightarrow$ `DoublyLinkedList`
  - `min_freq`: tracks minimum frequency currently in cache.
- Updating node access increments its frequency, moves node from `freq_map[f]` to `freq_map[f+1]`, and updates `min_freq`.

### Sample Input & Output
- **Input**: `cap = 2`, `put(1, 1)`, `put(2, 2)`, `get(1)`, `put(3, 3)`, `get(2)`
- **Output**: `get(1) = 1`, `get(2) = -1`

### Explanation
`1` has freq 2, `2` has freq 1. Inserting `3` evicts `2` (lowest freq).

### Python Implementation
- [`level_9_lfu_cache.py`](file:///c:/Users/chakr/Downloads/DSA/08-linked-list/level_9_lfu_cache.py)
