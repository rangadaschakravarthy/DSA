# Topic 11: Binary Trees (Level 1 to Level 9)

A binary tree is a non-linear data structure where each node has at most two children (left and right). Tree algorithms form the cornerstone of hierarchical structures, recursive search, and spatial partitions.

---

## Level-1: Binary Tree Traversals

### Question
Implement Inorder, Preorder, and Postorder traversals for a binary tree.

### Description / Explanation
- **Inorder**: Left $\rightarrow$ Root $\rightarrow$ Right
- **Preorder**: Root $\rightarrow$ Left $\rightarrow$ Right
- **Postorder**: Left $\rightarrow$ Right $\rightarrow$ Root

### Logic / Approach
Recursive DFS exploring node pointers in defined order.

### Sample Input & Output
- **Input**: Tree `1 -> right: 2 (left: 3)`
- **Output**:
  - Inorder: `[1, 3, 2]`
  - Preorder: `[1, 2, 3]`
  - Postorder: `[3, 2, 1]`

### Explanation
Traversing nodes following DFS node order.

### Python Implementation
- [`level_1_tree_traversals.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_1_tree_traversals.py)

---

## Level-2: Maximum Depth and Balanced Binary Tree

### Question
Find maximum depth of a tree and check if it is height-balanced.

### Description / Explanation
Height-balanced: height difference between left and right subtrees $\le 1$ for all nodes.

### Logic / Approach
Bottom-up DFS returning height or `-1` if unbalanced.

### Sample Input & Output
- **Input**: Tree `[3, 9, 20, null, null, 15, 7]`
- **Output**: `max_depth = 3`, `is_balanced = True`

### Explanation
Depth is 3; height difference at all nodes is $\le 1$.

### Python Implementation
- [`level_2_tree_depth_balance.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_2_tree_depth_balance.py)

---

## Level-3: Binary Tree Level Order Traversal

### Question
Return level order traversal of nodes (left to right, level by level).

### Description / Explanation
Breadth-First Search (BFS) using a Queue.

### Logic / Approach
Process queue level size elements at each iteration step.

### Sample Input & Output
- **Input**: `[3, 9, 20, null, null, 15, 7]`
- **Output**: `[[3], [9, 20], [15, 7]]`

### Explanation
Level 0: `[3]`, Level 1: `[9, 20]`, Level 2: `[15, 7]`.

### Python Implementation
- [`level_3_level_order_traversal.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_3_level_order_traversal.py)

---

## Level-4: Lowest Common Ancestor (LCA) of Binary Tree

### Question
Find the lowest common ancestor node of two target nodes $P$ and $Q$.

### Description / Explanation
The lowest node that has both $P$ and $Q$ as descendants.

### Logic / Approach
Recursive DFS: if node is $P$ or $Q$, return node. If both left and right return non-null, current node is LCA.

### Sample Input & Output
- **Input**: `root = 3`, `p = 5`, `q = 1`
- **Output**: `3`

### Explanation
Root `3` connects descendants `5` and `1`.

### Python Implementation
- [`level_4_lca_binary_tree.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_4_lca_binary_tree.py)

---

## Level-5: Binary Tree Right Side View

### Question
Return node values visible when looking at tree from the right side.

### Description / Explanation
Select the rightmost node at each depth level.

### Logic / Approach
BFS level-order traversal taking the last node of each level queue.

### Sample Input & Output
- **Input**: `[1, 2, 3, null, 5, null, 4]`
- **Output**: `[1, 3, 4]`

### Explanation
Level 1: 1, Level 2: 3, Level 3: 4.

### Python Implementation
- [`level_5_right_side_view.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_5_right_side_view.py)

---

## Level-6: Construct Binary Tree from Preorder & Inorder

### Question
Reconstruct binary tree from `preorder` and `inorder` arrays.

### Description / Explanation
First element of `preorder` is root. Root splits `inorder` into left and right subtrees.

### Logic / Approach
Use hashmap for $O(1)$ inorder index lookups, recursively build left and right subtrees.

### Sample Input & Output
- **Input**: `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`
- **Output**: Reconstructed root `3` with left child `9` and right child `20`.

### Explanation
Root `3` has left subtree `[9]` and right subtree `[15, 20, 7]`.

### Python Implementation
- [`level_6_construct_tree.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_6_construct_tree.py)

---

## Level-7: Binary Tree Maximum Path Sum

### Question
Find the maximum path sum of any non-empty path in a binary tree.

### Description / Explanation
Path can start and end at any node.

### Logic / Approach
Post-order DFS computing max single-branch path contribution while updating global maximum `node.val + left_max + right_max`.

### Sample Input & Output
- **Input**: `[-10, 9, 20, null, null, 15, 7]`
- **Output**: `42`

### Explanation
Path `15 -> 20 -> 7` yields max sum $15 + 20 + 7 = 42$.

### Python Implementation
- [`level_7_max_path_sum.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_7_max_path_sum.py)

---

## Level-8: Serialize and Deserialize Binary Tree

### Question
Convert a binary tree to a string and convert string back to identical binary tree.

### Description / Explanation
Preorder DFS using null markers `#`.

### Logic / Approach
- **Serialize**: Preorder traversal appending values and `#` for empty children.
- **Deserialize**: Consume tokens sequentially via iterator building tree recursively.

### Sample Input & Output
- **Input**: `[1, 2, 3, null, null, 4, 5]`
- **Output**: Serialized string `"1,2,#,#,3,4,#,#,5,#,#"`

### Explanation
Preserves tree structure accurately.

### Python Implementation
- [`level_8_serialize_deserialize_tree.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_8_serialize_deserialize_tree.py)

---

## Level-9: Vertical Order Traversal of Binary Tree

### Question
Return vertical order traversal of binary tree sorted by column index and row index.

### Description / Explanation
Assign coordinates `(row, col)` to nodes (root is `0, 0`).

### Logic / Approach
BFS to record coordinates, then sort by `col`, then `row`, then node value.

### Sample Input & Output
- **Input**: `[3, 9, 20, null, null, 15, 7]`
- **Output**: `[[9], [3, 15], [20], [7]]`

### Explanation
Col -1: `[9]`, Col 0: `[3, 15]`, Col 1: `[20]`, Col 2: `[7]`.

### Python Implementation
- [`level_9_vertical_order_traversal.py`](file:///c:/Users/chakr/Downloads/DSA/11-trees/level_9_vertical_order_traversal.py)
