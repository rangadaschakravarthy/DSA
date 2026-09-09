"""
Level 8: Binary Search Tree Iterator

Problem:
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree:
- `BSTIterator(root: TreeNode)` Initializes an object of the BSTIterator class.
- `next() -> int` Returns the next smallest number in the BST.
- `hasNext() -> bool` Returns True if there is a next number in the in-order traversal, otherwise False.

Time Complexity: O(1) average time per operation
Space Complexity: O(H) stack size
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


if __name__ == "__main__":
    root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    b_iter = BSTIterator(root)
    assert b_iter.next() == 3
    assert b_iter.next() == 7
    assert b_iter.hasNext() == True
    assert b_iter.next() == 9
    assert b_iter.hasNext() == True
    assert b_iter.next() == 15
    assert b_iter.next() == 20
    assert b_iter.hasNext() == False
    print("[PASS] Level 8 BST Iterator tests passed!")
