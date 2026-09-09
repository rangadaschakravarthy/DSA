"""
Level 4: Delete Node in a BST

Problem:
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference of the BST.

Time Complexity: O(H)
Space Complexity: O(H)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Case 1 & 2: Node has 0 or 1 child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Case 3: Node has 2 children -> Find inorder successor (min in right subtree)
        curr = root.right
        while curr.left:
            curr = curr.left

        root.val = curr.val
        root.right = delete_node(root.right, curr.val)

    return root


def inorder(root: TreeNode) -> list[int]:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    new_root = delete_node(root, 3)
    assert inorder(new_root) == [2, 4, 5, 6, 7]
    print("[PASS] Level 4 Delete Node in BST tests passed!")
