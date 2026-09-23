class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []
    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack or val<=self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        if self._stack:
            if self._stack.pop()==self._min_stack[-1]:
                self._min_stack.pop()
            
    def top(self) -> int:
        if self._stack:
            return self._stack[-1]

    def getMin(self) -> int:
        if self._min_stack:
            return self._min_stack[-1]
        
