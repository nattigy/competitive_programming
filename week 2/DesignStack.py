class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyStack:
    def __init__(self):
        self.head = Node()

    def top(self):
        return self.head.val

    def pop(self):
        if self.head.val == None:
            return None
        response = self.head.val
        self.head = self.head.next
        return response

    def push(self, val):
        if self.head.val == None:
            self.head.val = val
            return self.head.val
        self.head = Node(val, self.head)
        return self.head.val


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.top())
