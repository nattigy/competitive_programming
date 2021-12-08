# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, True)
            
            if not root.left and not root.right:
                return (1, True)
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            count = 0
            isSub = False
            if left[1] and right[1]:
                if root.left:
                    if root.left.val == root.val:
                        count += 1
                        isSub = True
                if root.right:
                    if root.right.val == root.val:
                        count += 1
                        isSub = True
                        
            if root.left and root.right and count == 1:
                count = 0
                isSub = False
                
            count = 1 if count > 0 else 0
            count += left[0]
            count += right[0]
            
            return (count, isSub)
            
        return dfs(root)[0]
        
        