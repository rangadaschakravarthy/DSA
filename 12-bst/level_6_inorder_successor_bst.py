"""
Level 6: Inorder Successor in BST

Problem:
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. 
If the given node has no in-order successor in the tree, return None.

Time Complexity: O(H)
Space Complexity: O(1)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_successor(root: TreeNode, p: TreeNode) -> TreeNode:
    successor = None
    curr = root
    
    while curr:
        if p.val < curr.val:
            successor = curr
            curr = curr.left
        else:
            curr = curr.right
            
    return successor


if __name__ == "__main__":
    n2 = TreeNode(2, TreeNode(1), TreeNode(3))
    root = TreeNode(5, n2, TreeNode(6))
    p = n2.right  # node 3
    succ = inorder_successor(root, p)
    assert succ.val == 5
    print("[PASS] Level 6 Inorder Successor in BST tests passed!")
