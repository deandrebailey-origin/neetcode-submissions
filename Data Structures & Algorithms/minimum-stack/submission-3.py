class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val

        #stack 0 min 1
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
        #stack 01 min 1
        #stack -1 0 1 min 0

    def pop(self) -> None:
        if not self.stack:
            return

        
        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

        #self.min = 0
        #stack 0 1 min 1

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

        #1 + 1 = 2

    def getMin(self) -> int:
        return self.min
        
