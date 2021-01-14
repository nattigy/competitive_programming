class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            self.stack1.append(x)
        elif len(self.stack2) > 0:
            self.stack2.append(x)
        elif len(self.stack1) > 0:
            self.stack1.insert(0, x)

    def pop(self) -> int:
        if len(self.stack1) == 1:
            val = self.stack1[0]
            self.stack1 = []
            return val
        if len(self.stack2) == 1:
            val = self.stack2[0]
            self.stack2 = []
            return val
        if len(self.stack2) > 0:
            val = self.stack2[0]
            self.stack2.pop(0)
            return val
        if len(self.stack1) > 0:
            self.stack2 = []
            for i in range(len(self.stack1)):
                self.stack2.insert(0, self.stack1[i])
            self.stack1 = []
            val = self.stack2[0]
            self.stack2.pop(0)
            return val

    def peek(self) -> int:
        if len(self.stack1) == 1:
            val = self.stack1[0]
            return val
        if len(self.stack2) == 1:
            val = self.stack2[0]
            return val
        if len(self.stack2) > 0:
            val = self.stack2[0]
            return val
        if len(self.stack1) > 0:
            self.stack2 = []
            for i in range(len(self.stack1)):
                self.stack2.insert(0, self.stack1[i])
            self.stack1 = []
            val = self.stack2[0]
            return val

    def empty(self) -> bool:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()