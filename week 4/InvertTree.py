# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.right, root.left = root.left, root.right
        self.invert(root.left)
        self.invert(root.right)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root
