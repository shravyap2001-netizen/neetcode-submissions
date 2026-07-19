class MinStack:

    def __init__(self):
        self.mainst = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.mainst.append(val)
        if not self.MinStack:
            self.MinStack.append(val)
        else:
            self.MinStack.append(min(val, self.MinStack[-1]))
        # if not self.MinStack or self.MinStack[-1] >= val:
            # self.MinStack.append(val)
        # return 'null'

    def pop(self) -> None:
        a = self.mainst.pop()
        # if a == self.MinStack[-1]:
        self.MinStack.pop()
        # return 'null'

    def top(self) -> int:
        return self.mainst[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
