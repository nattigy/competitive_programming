# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def count(self, head: ListNode) -> int:
        i = 0
        c = head
        while c:
            c = c.next
            i += 1
        return i

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        node = head
        prev_node = None

        while node:
            i = 0
            node = self.reverseList(node, k)
            while node and i < k:
                if prev_node == None:
                    prev_node = ListNode(node.val)
                else:
                    c_node = node.val
                    prev_node = self.addAtTail(prev_node, ListNode(c_node))
                node = node.next
                i += 1
        return prev_node

    def reverseList(self, head: ListNode, k: int) -> ListNode:
        node = head
        count = self.count(head)
        p = None
        i = 0
        r = None
        if count >= k:
            while node and i < k:
                nextt = node.next
                node.next = p
                p = node
                node = nextt
                i += 1
            r = self.addAtTail(p, node)
        else:
            r = head
        return r

    def addAtTail(self, head: ListNode, new_node: ListNode) -> None:
        node = head
        while node.next:
            node = node.next
        node.next = new_node
        return head
