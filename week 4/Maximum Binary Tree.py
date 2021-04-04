# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMax(self, nums: List[int]) -> [int]:
        index = 0
        mx = 0
        for i in range(len(nums)):
            if mx < nums[i]:
                mx = nums[i]
                index = i
        return [mx, index]

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        root = None
        val = self.findMax(nums)
        mx = val[0]
        index = val[1]
        
        
        root = TreeNode(mx)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        
        if index == len(nums) -1:
            root.right = None
        else:
            root.right = self.constructMaximumBinaryTree(nums[index+1:])

        return root
