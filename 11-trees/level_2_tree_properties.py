"""
Level 2: Structural Tree Properties & Lowest Common Ancestor

Topics Covered:
1. Maximum Depth of Binary Tree O(N)
2. Invert Binary Tree O(N)
3. Lowest Common Ancestor (LCA) O(N)

Complexity:
- Time Complexity: O(N) single traversal.
- Space Complexity: O(H) recursion call stack depth (H = height of tree).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """Calculates maximum depth (height) of a binary tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def invert_tree(root: TreeNode) -> TreeNode:
    """Inverts a binary tree in-place (mirror image)."""
    if not root:
        return None
        
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor (LCA) of nodes p and q in a binary tree.
    """
    if not root or root == p or root == q:
        return root
        
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root  # Node root is the LCA since p and q are in different subtrees
        
    return left if left else right


if __name__ == "__main__":
    # Tree:
    #      3
    #     / \
    #    5   1
    #   / \
    #  6   2
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node5 = TreeNode(5, node6, node2)
    node1 = TreeNode(1)
    root = TreeNode(3, node5, node1)
    
    # Test Max Depth
    assert max_depth(root) == 3
    
    # Test LCA
    assert lowest_common_ancestor(root, node5, node1) == root
    assert lowest_common_ancestor(root, node6, node2) == node5
    
    # Test Invert Tree
    inv_root = invert_tree(root)
    assert inv_root.left.val == 1
    assert inv_root.right.val == 5
    
    print("[SUCCESS] All Level 2 Tree Properties tests passed!")
