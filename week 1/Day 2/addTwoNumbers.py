# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    newList = ListNode(0)
    carry = 0
    summ = 0
    head = newList
    head2 = newList

    while l1 != None and l2 != None:
        summ = l1.val + l2.val + carry
        newList.val = summ % 10
        carry = summ // 10
        l1 = l1.next
        l2 = l2.next
        if l1 != None or l2 != None:
            newList.next = ListNode(0)
            newList = newList.next

    if l1 != None:
        while l1 != None:
            newList.val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            l1 = l1.next
            if l1 != None:
                newList.next = ListNode(0)
                newList = newList.next

    if l2 != None:
        while l2 != None:
            newList.val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l2 = l2.next
            if l2 != None:
                newList.next = ListNode(0)
                newList = newList.next

    if carry != 0:
        newList.next = ListNode(0)
        newList = newList.next
        newList.val = carry

    res = []
    i = 0
    while head != None:
        res.append(head.val)
        head = head.next
        i += 1

    print(res)
    return head2


list1 = ListNode(3, ListNode(7))
list2 = ListNode(9, ListNode(2))
print(addTwoNumbers(list1, list2))