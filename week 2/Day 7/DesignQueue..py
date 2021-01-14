class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyQueue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def enQueue(self, val):
        if self.head.val == None:
            self.head.val = val
            return self.head.val
        self.tail = Node(val, self.tail)
        return self.tail

    def deQueue(self):
        if self.head.val == None:
            return None
        val = self.head
        self.head = self.head.next
        return val

    def empty(self):
        return self.head.val is None


queue = MyQueue()
print(queue.enQueue(1))
print(queue.empty())