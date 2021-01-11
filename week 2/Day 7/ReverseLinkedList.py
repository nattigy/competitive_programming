class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        p = None
        while node:
            next = node.next
            node.next = p
            p = node
            node = next

        return p


sln = Solution()
sln.reverseList(ListNode(1, ListNode(5, ListNode(9, ListNode(4)))))
