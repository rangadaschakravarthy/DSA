"""
Level 2: Inorder Monotonicity & K-th Smallest in BST

Topics Covered:
1. K-th Smallest Element in a BST O(H + K)

Monotonic Invariant:
An INORDER traversal of a BST visits nodes in strictly INCREASING sorted order!
We can stop as soon as we visit the k-th node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Finds the 1-indexed k-th smallest element in a BST.
    Uses iterative inorder traversal with a stack to stop early after k visits.
    """
    stack = []
    curr = root
    count = 0
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
            
        curr = stack.pop()
        count += 1
        
        if count == k:
            return curr.val
            
        curr = curr.right
        
    return -1


if __name__ == "__main__":
    # BST:
    #      3
    #     / \
    #    1   4
    #     \
    #      2
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 2) == 2
    assert kth_smallest(root, 3) == 3
    assert kth_smallest(root, 4) == 4
    
    print("[SUCCESS] All Level 2 K-th Smallest BST tests passed!")
