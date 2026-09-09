"""
Level 6: Construct Binary Tree from Preorder and Inorder Traversal

Problem:
Given two integer arrays preorder and inorder where preorder is the preorder traversal 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Time Complexity: O(N)
Space Complexity: O(N) hash map + recursion stack
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = 0

    def array_to_tree(left, right):
        nonlocal pre_idx
        if left > right:
            return None

        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)

        in_idx = inorder_map[root_val]

        root.left = array_to_tree(left, in_idx - 1)
        root.right = array_to_tree(in_idx + 1, right)

        return root

    return array_to_tree(0, len(inorder) - 1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = build_tree(preorder, inorder)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    print("[PASS] Level 6 Construct Binary Tree tests passed!")
