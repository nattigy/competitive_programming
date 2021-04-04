# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        while l1 and l2:
            if l1.val <= l2.val:
                node = head
                if node is None:
                    head = ListNode(l1.val)
                    tail = head
                else:
                    tail.next = ListNode(l1.val)
                    tail = tail.next
                l1 = l1.next
            else:
                node = head
                if node is None:
                    head = ListNode(l2.val)
                    tail = head
                else:
                    tail.next = ListNode(l2.val)
                    tail = tail.next
                l2 = l2.next
        if l1 != None:
            if head == None:
                head = l1
            else:
                tail.next = l1
        if l2 != None:
            if head == None:
                head = l2
            else:
                tail.next = l2
        return head
