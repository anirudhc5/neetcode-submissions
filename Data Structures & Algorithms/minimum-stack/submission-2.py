import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            if val <= self.mins[-1]:
                self.mins.append(val)
        
    def top(self) -> int:
        return self.stack[-1]

    def pop(self) -> None:
        if self.top() == self.mins[-1]:
            self.mins.pop()
        self.stack.pop()
        

    def getMin(self) -> int:
        # print(self.stack, self.mins)
        return self.mins[-1]
        
