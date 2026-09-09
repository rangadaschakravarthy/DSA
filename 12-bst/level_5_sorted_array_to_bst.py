"""
Level 5: Convert Sorted Array to Height Balanced Binary Search Tree

Problem:
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

Time Complexity: O(N)
Space Complexity: O(log N) recursion depth
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]) -> TreeNode:
    if not nums:
        return None
        
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    
    return root


def is_balanced(root: TreeNode) -> bool:
    def height(node):
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        if lh == -1 or rh == -1 or abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)
    return height(root) != -1


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    bst_root = sorted_array_to_bst(nums)
    assert bst_root.val == 0
    assert is_balanced(bst_root) == True
    print("[PASS] Level 5 Sorted Array to Height-Balanced BST tests passed!")
