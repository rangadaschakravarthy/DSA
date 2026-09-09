# Topic 12: Binary Search Trees (Level 1 to Level 9)

A Binary Search Tree (BST) is a binary tree with the invariant property: for any node, all left subtree values are strictly smaller, and all right subtree values are strictly larger.

---

## Level-1: Search, Insert, and Validate BST

### Question
Implement search, insertion, and validation operations on a Binary Search Tree.

### Description / Explanation
Validate that for every node, `low < node.val < high`.

### Logic / Approach
Pass valid ranges `(low, high)` recursively down the tree.

### Sample Input & Output
- **Input**: Tree `[4, 2, 7, 1, 3]`
- **Output**: `is_valid = True`, `search(2).val = 2`

### Explanation
Left subtree values $< 4$ and right subtree values $> 4$.

### Python Implementation
- [`level_1_bst_basics_validation.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_1_bst_basics_validation.py)

---

## Level-2: Kth Smallest Element in a BST

### Question
Find the $K$-th smallest value (1-indexed) in a BST.

### Description / Explanation
An Inorder traversal of a BST visits nodes in strictly sorted ascending order.

### Logic / Approach
Iterative inorder traversal using stack; return value when $K$-th node is popped.

### Sample Input & Output
- **Input**: Tree `[3, 1, 4, null, 2]`, `k = 1`
- **Output**: `1`

### Explanation
Sorted sequence: `[1, 2, 3, 4]`. 1st smallest $= 1$.

### Python Implementation
- [`level_2_kth_smallest_bst.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_2_kth_smallest_bst.py)

---

## Level-3: Lowest Common Ancestor of a BST

### Question
Find LCA of nodes $P$ and $Q$ in a BST.

### Description / Explanation
Exploit BST ordering: if both $P, Q < \text{node.val}$, LCA is in left subtree; if both $>$, right subtree.

### Logic / Approach
Iterative search stepping left or right until values split around current node.

### Sample Input & Output
- **Input**: Root `6`, $P=2, Q=8$
- **Output**: `6`

### Explanation
2 is in left subtree, 8 is in right subtree of root 6.

### Python Implementation
- [`level_3_lca_bst.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_3_lca_bst.py)

---

## Level-4: Delete Node in a BST

### Question
Delete a key from a BST while maintaining the BST property.

### Description / Explanation
If target node has 2 children, replace node value with its in-order successor (minimum value in right subtree) and delete successor.

### Logic / Approach
Recursive search and structural adjustment.

### Sample Input & Output
- **Input**: Tree `[5,3,6,2,4,null,7]`, `key = 3`
- **Output**: Replaced tree with inorder `[2, 4, 5, 6, 7]`

### Explanation
Node 3 replaced by successor 4.

### Python Implementation
- [`level_4_delete_node_bst.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_4_delete_node_bst.py)

---

## Level-5: Convert Sorted Array to Height-Balanced BST

### Question
Convert sorted array into a height-balanced BST.

### Description / Explanation
Height-balanced: depth of the two subtrees of every node never differs by more than 1.

### Logic / Approach
Pick middle element as root, recursively build left subtree from left half, right subtree from right half.

### Sample Input & Output
- **Input**: `[-10, -3, 0, 5, 9]`
- **Output**: Root `0` with balanced left and right subtrees.

### Explanation
Middle element `0` ensures balanced left `[-10, -3]` and right `[5, 9]`.

### Python Implementation
- [`level_5_sorted_array_to_bst.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_5_sorted_array_to_bst.py)

---

## Level-6: Inorder Successor in BST

### Question
Find the node with the smallest value greater than `p.val` in a BST.

### Description / Explanation
Inorder successor is the next node visited after $P$ during inorder traversal.

### Logic / Approach
If `p.val < curr.val`, record `curr` as candidate successor and move left; else move right.

### Sample Input & Output
- **Input**: Root `5`, $P=3$
- **Output**: `5`

### Explanation
Node 5 is the smallest element greater than 3.

### Python Implementation
- [`level_6_inorder_successor_bst.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_6_inorder_successor_bst.py)

---

## Level-7: Recover Binary Search Tree

### Question
Two node values in a BST were accidentally swapped. Recover tree without changing structure.

### Description / Explanation
Inorder traversal of BST should be monotonically increasing.

### Logic / Approach
Identify two out-of-order nodes during inorder traversal where `prev.val > curr.val` and swap their values back.

### Sample Input & Output
- **Input**: Swapped tree `[1, 3, null, null, 2]`
- **Output**: Recovered tree `[3, 1, null, null, 2]` with inorder `[1, 2, 3]`

### Explanation
Nodes 3 and 1 were swapped; restoring them fixes BST property.

### Python Implementation
- [`level_7_recover_bst.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_7_recover_bst.py)

---

## Level-8: BST Iterator

### Question
Design an iterator over the in-order traversal of a BST with $O(1)$ average time and $O(H)$ space.

### Description / Explanation
Controlled stack simulation of inorder traversal.

### Logic / Approach
Initialize stack pushing all left children. `next()` pops stack top and pushes left children of right child.

### Sample Input & Output
- **Input**: `[7, 3, 15, null, null, 9, 20]`
- **Output**: Sequence of `next()` calls: `3, 7, 9, 15, 20`

### Explanation
Produces elements in ascending order.

### Python Implementation
- [`level_8_bst_iterator.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_8_bst_iterator.py)

---

## Level-9: Count of Smaller Numbers After Self

### Question
For each element `nums[i]`, count the number of smaller elements to its right.

### Description / Explanation
Augmented BST / Modified MergeSort inversion counting.

### Logic / Approach
During MergeSort merge step, when an element from right half is smaller than element from left half, increment right count.

### Sample Input & Output
- **Input**: `[5, 2, 6, 1]`
- **Output**: `[2, 1, 1, 0]`

### Explanation
Right of 5: 2 and 1 are smaller (count 2). Right of 2: 1 is smaller (count 1). Right of 6: 1 is smaller (count 1). Right of 1: none (count 0).

### Python Implementation
- [`level_9_count_smaller_after_self.py`](file:///c:/Users/chakr/Downloads/DSA/12-bst/level_9_count_smaller_after_self.py)
