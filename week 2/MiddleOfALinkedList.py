# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        node = head
        i = 0
        while node:
            node = node.next
            i += 1
        return i

    def middleNode(self, head: ListNode) -> ListNode:
        # node = head
        # length = self.count(head)
        # if length == 1:
        #     return head
        # for i in range(length//2):
        #     node = node.next
        slow = head
        fast = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        return slow
