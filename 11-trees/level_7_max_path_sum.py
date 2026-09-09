"""
Level 7: Binary Tree Maximum Path Sum

Problem:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
Find the maximum path sum of any non-empty path.

Time Complexity: O(N)
Space Complexity: O(H) recursion depth
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left_max = max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)

        # Price of current path passing through node
        current_path_sum = node.val + left_max + right_max
        max_sum = max(max_sum, current_path_sum)

        # Return max contribution to parent
        return node.val + max(left_max, right_max)

    dfs(root)
    return max_sum


if __name__ == "__main__":
    # Tree: -10 -> left: 9, right: 20 (left: 15, right: 7)
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(root) == 42  # 15 + 20 + 7
    print("[PASS] Level 7 Binary Tree Maximum Path Sum tests passed!")
