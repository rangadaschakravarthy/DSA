"""
Level 7: Recover Binary Search Tree

Problem:
You are given the root of a binary search tree (BST), where the values of exactly two nodes 
were swapped by mistake. Recover the tree without changing its structure.

Time Complexity: O(N)
Space Complexity: O(H) recursion / O(1) Morris traversal
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recover_tree(root: TreeNode) -> None:
    first = second = prev = None

    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return
        inorder(node.left)

        if prev and prev.val > node.val:
            if not first:
                first = prev
            second = node

        prev = node
        inorder(node.right)

    inorder(root)
    if first and second:
        first.val, second.val = second.val, first.val


def get_inorder(root: TreeNode) -> list[int]:
    return get_inorder(root.left) + [root.val] + get_inorder(root.right) if root else []


if __name__ == "__main__":
    # Swapped 3 and 1
    root = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
    recover_tree(root)
    assert get_inorder(root) == [1, 2, 3]
    print("[PASS] Level 7 Recover Binary Search Tree tests passed!")
