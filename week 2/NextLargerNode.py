# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        current = head
        while current:
            node = current
            while node:
                if current.val < node.val:
                    res.append(node.val)
                    break
                node = node.next
                if node == None:
                    res.append(0)
            current = current.next
        return res


sln = Solution()
print(sln.nextLargerNodes(ListNode(2, ListNode(1, ListNode(5)))))
