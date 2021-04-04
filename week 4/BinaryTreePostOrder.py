# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res
        stack = [root]
        while stack:
            if root.left:
                stack.append(root.left)
                temp = root
                root = root.left
                temp.left = None
                continue
            if root.right:
                stack.append(root.right)
                temp = root
                root = root.right
                temp.right = None
                continue
            res.append(root.val)
            root = stack.pop()
        return res
    
    def postorderTraversalR(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res