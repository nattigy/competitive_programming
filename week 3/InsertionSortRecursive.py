# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.smallest = None
        
    def insert(self, current) -> ListNode:
        if current == None:
            return None
        if current.next == None:
            self.smallest = current
            return current
        sm = self.insert(current.next)
        current.next = None
        if current.val < sm.val:
            current.next = sm
            self.smallest = current
            sm = current
        else:
            n = sm
            while n:
                if n.next == None:
                    n.next = current
                    break
                if current.val <= n.next.val:
                    temp = n.next
                    n.next = current
                    current.next = temp
                    break
                n = n.next
        return sm 
        
    def insertionSortList(self, head: ListNode) -> ListNode:
        self.insert(head)
        return self.smallest
        