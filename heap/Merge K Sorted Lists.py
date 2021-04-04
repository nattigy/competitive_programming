# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ll = []
        head = None
        res = None
        for l in lists:
            temp = []
            while l:
                temp.append(l.val)
                l = l.next
            heappush(ll, temp)
        while ll:
            pop = heappop(ll)
            if len(pop) > 0:
                if not head:
                    head = ListNode(pop[0])
                    res = head
                else:
                    head.next = ListNode(pop[0])
                    head = head.next
                pop.pop(0)
            if len(pop) > 0:
                heappush(ll, pop)
            
        return res
                
