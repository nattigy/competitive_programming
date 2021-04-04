# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def count(self, head):
        node = head
        i = 0
        while node:
            node = node.next
            i += 1
        return i

    def reverse(self, head):
        node = head
        new_head = []
        while node:
            new_head.append(node.val)
            node = node.next
        res_head = None
        res = None
        for i in range(len(new_head) - 1, -1, -1):
            if i == len(new_head) - 1:
                res_head = ListNode(new_head[i])
                res = res_head
            else:
                res_head.next = ListNode(new_head[i])
                res_head = res_head.next
        return res

    def isPalindrome(self, head: ListNode) -> bool:
        count = self.count(head)
        if count <= 1:
            return True
        reverse = self.reverse(head)
        top = head
        i = 0
        while reverse.val == top.val:
            if i == (count // 2):
                return True
            top = top.next
            reverse = reverse.next
            i += 1
        return False