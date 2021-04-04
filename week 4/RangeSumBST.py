# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        if low <= root.val <= high:
            self.res += root.val
        if root.val > high and root.left:
            self.rangeSumBST(root.left, low, high)
        if root.val < low and root.right:
            self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            if root.left:
                self.rangeSumBST(root.left, low, high)
            if root.right:
                self.rangeSumBST(root.right, low, high)
        return self.res