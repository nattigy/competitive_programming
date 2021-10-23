#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx = [0]
        left = self.dfs(root.left, maxx)
        right = self.dfs(root.right, maxx)
        summ = left + right
        return max(maxx[0], summ)
    def dfs(self, root, maxx):
        if not root:
            return 0
        left = self.dfs(root.left, maxx)
        right = self.dfs(root.right, maxx)
        summ = left + right
        maxx[0] = max(maxx[0], summ)
        return 1+left if left > right else 1+right
# @lc code=end

