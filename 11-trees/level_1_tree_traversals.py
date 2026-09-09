"""
Level 1: Binary Tree Traversals (DFS & BFS)

Topics Covered:
1. Inorder, Preorder, Postorder Traversals (DFS O(N))
2. Level Order Traversal (BFS O(N) using collections.deque)

Complexity:
- Time Complexity: O(N) visits each node once.
- Space Complexity: O(H) call stack for DFS (H = height), O(W) queue for BFS (W = max width).
"""

from collections import deque

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> list[int]:
    """Inorder DFS: Left -> Root -> Right."""
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res


def preorder_traversal(root: TreeNode) -> list[int]:
    """Preorder DFS: Root -> Left -> Right."""
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res


def level_order_traversal(root: TreeNode) -> list[list[int]]:
    """Level Order BFS: Returns nodes level by level."""
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
        
    return result


if __name__ == "__main__":
    # Construct Binary Tree:
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    
    # Test Inorder
    assert inorder_traversal(root) == [4, 2, 5, 1, 3]
    
    # Test Preorder
    assert preorder_traversal(root) == [1, 2, 4, 5, 3]
    
    # Test Level Order
    assert level_order_traversal(root) == [[1], [2, 3], [4, 5]]
    
    print("[SUCCESS] All Level 1 Tree Traversals tests passed!")
