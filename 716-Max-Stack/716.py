import sys
class MaxStack:
    MIN_INT = -sys.maxsize - 1
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        ans = self.stack[-1]
        self.stack = self.stack[:-1]
        return ans

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        currMax = MaxStack.MIN_INT
        for i in self.stack:
            currMax = i if i >= currMax else currMax
        return currMax

    def popMax(self) -> int:
        if len(self.stack) == 0:
            return 0
        elif len(self.stack) == 1:
            ans = self.stack[0]
            self.stack = []
            return ans

        
        currMax = MaxStack.MIN_INT
        for i in self.stack:
            currMax = i if i >= currMax else currMax
        # maxIdx = self.stack.rindex(currMax)
        maxIdx = len(self.stack) - 1 - self.stack[::-1].index(currMax)
        if maxIdx == len(self.stack) - 1:
            self.stack = self.stack[:-1]
        elif maxIdx == 0:
            self.stack = self.stack[1:]
        else:  
            self.stack = self.stack[:maxIdx] + self.stack[maxIdx + 1:]
        return currMax