"""
Level 2: Maximum Depth and Balanced Binary Tree

Problem:
1. Max Depth: Find height/maximum depth of a binary tree.
2. Balanced Binary Tree: Check if height difference between left & right subtree of any node is at most 1.

Time Complexity: O(N)
Space Complexity: O(H) recursion height
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_balanced(root: TreeNode) -> bool:
    def check_height(node):
        if not node:
            return 0
        left_h = check_height(node.left)
        if left_h == -1:
            return -1
        right_h = check_height(node.right)
        if right_h == -1 or abs(left_h - right_h) > 1:
            return -1
        return 1 + max(left_h, right_h)

    return check_height(root) != -1


if __name__ == "__main__":
    # Balanced tree: 3 -> left: 9, right: 20 (left: 15, right: 7)
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3
    assert is_balanced(root) == True

    # Unbalanced tree
    unbalanced = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert is_balanced(unbalanced) == False
    print("[PASS] Level 2 Tree Depth and Balance tests passed!")
