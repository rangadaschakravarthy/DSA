"""
Level 8: Serialize and Deserialize Binary Tree

Problem:
Design an algorithm to serialize and deserialize a binary tree into/from a string representation.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        vals = []
        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> TreeNode:
        vals = iter(data.split(","))
        def dfs():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert codec.serialize(deserialized) == serialized
    print("[PASS] Level 8 Serialize and Deserialize Binary Tree tests passed!")
