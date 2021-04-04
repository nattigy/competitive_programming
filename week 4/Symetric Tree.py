class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        if (root.left and not root.right) or (root.right and not root.left):
            return False
        half1 = []
        half2 = []
        stack = []
        stack2 = []
        stack.append(root.left)
        stack2.append(root.right)
        while stack:
            pop = stack.pop()
            if pop.right:
                stack.append(pop.right)
            else:
                half1.append(1)
            if pop.left:
                stack.append(pop.left)
            else:
                half1.append(0)
            half1.append(pop.val)

        while stack2:
            pop = stack2.pop()
            if pop.left:
                stack2.append(pop.left)
            else:
                half2.append(1)
            if pop.right:
                stack2.append(pop.right)
            else:
                half2.append(0)
            half2.append(pop.val)
        return half1 == half2
