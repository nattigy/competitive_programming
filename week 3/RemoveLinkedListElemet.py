# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        node = head
        prev = None
        i = 0
        while node:
            if node.val == val and i == 0:
                head = node.next
                prev = head
            elif node.val == val:
                prev.next = prev.next.next
                i += 1
            else:
                prev = node
                i += 1
            node = node.next
        return head
