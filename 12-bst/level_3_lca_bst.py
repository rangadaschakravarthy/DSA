"""
Level 3: Lowest Common Ancestor of a Binary Search Tree

Problem:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes p and q.

Time Complexity: O(H)
Space Complexity: O(1) iterative space
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
    return None


if __name__ == "__main__":
    n2 = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    n8 = TreeNode(8, TreeNode(7), TreeNode(9))
    root = TreeNode(6, n2, n8)
    
    assert lowest_common_ancestor_bst(root, TreeNode(2), TreeNode(8)).val == 6
    assert lowest_common_ancestor_bst(root, TreeNode(2), TreeNode(4)).val == 2
    print("[PASS] Level 3 LCA of BST tests passed!")
