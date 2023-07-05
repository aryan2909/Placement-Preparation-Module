class MyQueue:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)

    def transfer_elements(self):
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())

    def pop(self) -> int:
        if not self.dequeue_stack:
            self.transfer_elements()
        return self.dequeue_stack.pop()

    def peek(self) -> int:
        if not self.dequeue_stack:
            self.transfer_elements()
        return self.dequeue_stack[-1]

    def empty(self) -> bool:
        return not self.enqueue_stack and not self.dequeue_stack
