"""
Level 1: Binary Tree Traversals (Inorder, Preorder, Postorder)

Problem:
Implement recursive and iterative tree traversals: Inorder (LNR), Preorder (NLR), and Postorder (LRN).

Time Complexity: O(N)
Space Complexity: O(H) recursion stack height
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> list[int]:
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
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res


def postorder_traversal(root: TreeNode) -> list[int]:
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    dfs(root)
    return res


if __name__ == "__main__":
    # Tree: 1 -> right: 2 -> left: 3
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    assert inorder_traversal(root) == [1, 3, 2]
    assert preorder_traversal(root) == [1, 2, 3]
    assert postorder_traversal(root) == [3, 2, 1]
    print("[PASS] Level 1 Binary Tree Traversals tests passed!")
