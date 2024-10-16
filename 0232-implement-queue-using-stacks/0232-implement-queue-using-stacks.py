class MyQueue:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.popped = 0

    def push(self, x: int) -> None:
        self.size += 1
        self.stack.append(x)

    def pop(self) -> int:
        self.size -= 1
        self.popped += 1
        return self.stack[self.popped - 1]
        pass

    def peek(self) -> int:
        return self.stack[self.popped]

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
