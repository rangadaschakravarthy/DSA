"""
Level 5: Binary Tree Right Side View

Problem:
Given the root of a binary tree, imagine yourself standing on the right side of it. 
Return the values of the nodes you can see ordered from top to bottom.

Time Complexity: O(N)
Space Complexity: O(W) queue width or recursion height
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode) -> list[int]:
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return result


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root) == [1, 3, 4]
    print("[PASS] Level 5 Binary Tree Right Side View tests passed!")
