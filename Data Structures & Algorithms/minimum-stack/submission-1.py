class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_value) == 0:
            self.min_value.append(val)
        elif val <= self.min_value[-1]:
            self.min_value.append(val)
        return None
        
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_value[-1]:
            self.min_value.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.min_value) == 0:
            return None
        return self.min_value[-1]