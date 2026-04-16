class MinStack:

    def __init__(self):
        self.min_val = None
        self.min_stack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val == None or self.min_val >= val:
            self.min_val = val
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # Min val was popped
        if val == self.min_val:
            self.min_stack.pop()
            self.min_val = self.min_stack[-1] if len(self.min_stack) > 0 else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
        
