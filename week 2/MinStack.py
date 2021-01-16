class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            if self.stack[len(self.stack) - 1][1] > x:
                self.stack.append((x, x))
            else:
                self.stack.append((x, self.stack[len(self.stack) - 1][1]))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()