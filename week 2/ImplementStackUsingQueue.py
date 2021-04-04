class MyStack:

    def __init__(self):
        self.qu1 = []
        self.qu2 = []

    def push(self, x: int) -> None:
        if len(self.qu1) >= 0 and len(self.qu2) == 0:
            self.qu1.append(x)
        elif len(self.qu1) == 0 and len(self.qu2) > 0:
            self.qu2.append(x)
        

    def pop(self) -> int:
        if len(self.qu1) == 0 and len(self.qu2) == 0:
            return None
        if len(self.qu1) > 0:
            for i in range(len(self.qu1)):
                if i == len(self.qu1)-1:
                    res = self.qu1[i]
                    self.qu1 = []
                    return res
                self.qu2.append(self.qu1[i])
        else:
            for i in range(len(self.qu2)):
                if i == len(self.qu2)-1:
                    res = self.qu2[i]
                    self.qu2 = []
                    return res
                self.qu1.append(self.qu2[i])
        
        
    def top(self) -> int:
        if len(self.qu1) == 0 and len(self.qu2) == 0:
            return None
        if len(self.qu1) > 0:
            for i in range(len(self.qu1)):
                if i == len(self.qu1)-1:
                    res = self.qu1[i]
                    self.qu2.append(self.qu1[i])
                    self.qu1 = []
                    return res
                self.qu2.append(self.qu1[i])
        else:
            for i in range(len(self.qu2)):
                if i == len(self.qu2)-1:
                    res = self.qu2[i]
                    self.qu1.append(self.qu2[i])
                    self.qu2 = []
                    return res
                self.qu1.append(self.qu2[i])
        

    def empty(self) -> bool:
        return len(self.qu1) == 0 and len(self.qu2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()