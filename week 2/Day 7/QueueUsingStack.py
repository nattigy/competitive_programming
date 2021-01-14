class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyQueue:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        if self.head == None:
            self.head = Node(x)
            return
        c_node = self.head
        while c_node.next:
            c_node = c_node.next
        c_node.next = Node(x)

    def pop(self) -> int:
        if self.head == None:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self) -> int:
        if self.head == None:
            return None
        return self.head.val

    def empty(self) -> bool:
        if self.head == None:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()