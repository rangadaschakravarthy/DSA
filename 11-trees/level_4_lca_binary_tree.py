"""
Level 4: Lowest Common Ancestor of a Binary Tree

Problem:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

Time Complexity: O(N)
Space Complexity: O(H) call stack depth
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
        
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right


if __name__ == "__main__":
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    root = TreeNode(3, n5, n1)
    assert lowest_common_ancestor(root, n5, n1) == root
    print("[PASS] Level 4 Lowest Common Ancestor tests passed!")
