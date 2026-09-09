"""
Level 1: Binary Search Tree Invariants & Validation

Topics Covered:
1. Validate Binary Search Tree O(N)
2. Search in Binary Search Tree O(H)

BST Invariant:
For every node in a BST:
- All nodes in left subtree have value strictly LESS than node.val.
- All nodes in right subtree have value strictly GREATER than node.val.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    """
    Validates if binary tree is a valid Binary Search Tree.
    Propagates valid (low, high) bounds down to child subtrees.
    """
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
            
        if not (low < node.val < high):
            return False
            
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
    return validate(root)


def search_bst(root: TreeNode, val: int) -> TreeNode:
    """
    Searches for a node with target value in a BST.
    Returns node if found, else None.
    """
    curr = root
    while curr:
        if curr.val == val:
            return curr
        elif val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return None


if __name__ == "__main__":
    # Test Valid BST:
    #      2
    #     / \
    #    1   3
    valid_root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(valid_root) is True
    
    # Test Invalid BST:
    #      5
    #     / \
    #    1   4
    #       / \
    #      3   6 (4 is child of 5, but has left child 3 < 5! However 4 < 5 so invalid)
    invalid_root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(invalid_root) is False
    
    # Test Search BST
    found = search_bst(valid_root, 3)
    assert found is not None and found.val == 3
    assert search_bst(valid_root, 10) is None
    
    print("[SUCCESS] All Level 1 BST Validation tests passed!")
