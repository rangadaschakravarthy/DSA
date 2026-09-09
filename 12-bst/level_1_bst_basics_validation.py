"""
Level 1: Search, Insert, and Validate Binary Search Tree (BST)

Problem:
1. Search in BST: Return node matching value or None.
2. Insert into BST: Insert value adhering to BST property.
3. Validate BST: Check if a binary tree is a valid BST (left < root < right for all nodes).

Time Complexity: O(H) where H is height of BST
Space Complexity: O(H) recursion depth
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root: TreeNode, val: int) -> TreeNode:
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)


def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


def is_valid_bst(root: TreeNode) -> bool:
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root)


if __name__ == "__main__":
    # Valid BST: 4 -> left: 2, right: 7
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    assert is_valid_bst(root) == True
    assert search_bst(root, 2).val == 2
    
    # Invalid BST: 5 -> left: 1, right: 4 (left: 3, right: 6)
    invalid_root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(invalid_root) == False
    print("[PASS] Level 1 BST Basics and Validation tests passed!")
