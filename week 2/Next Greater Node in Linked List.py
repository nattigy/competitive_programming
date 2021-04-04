# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        i = 0
        res.append(0)
        stack.append((head.val, i))
        head = head.next
        while head:
            res.append(0)
            i += 1
            while stack:
                if stack[-1][0] < head.val:
                    pop = stack.pop()
                    res[pop[1]] = head.val
                else:
                    break
            stack.append((head.val, i))
            head = head.next
        return res
