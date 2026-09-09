"""
Level 9: Vertical Order Traversal of a Binary Tree

Problem:
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
Nodes at same column and row should be sorted by value.

Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    # col -> list of (row, val)
    nodes = defaultdict(list)
    queue = deque([(root, 0, 0)])  # node, row, col

    while queue:
        node, row, col = queue.popleft()
        nodes[col].append((row, node.val))

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    result = []
    for col in sorted(nodes.keys()):
        # Sort by row first, then value
        sorted_nodes = sorted(nodes[col], key=lambda x: (x[0], x[1]))
        result.append([val for row, val in sorted_nodes])

    return result


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert vertical_traversal(root) == [[9], [3, 15], [20], [7]]
    print("[PASS] Level 9 Vertical Order Traversal tests passed!")
