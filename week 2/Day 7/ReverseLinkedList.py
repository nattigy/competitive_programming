class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
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


sln = Solution()
sln.reverseList(ListNode(1, ListNode(5, ListNode(9, ListNode(4)))))
