class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        print(self.items[-1])

    def is_empty(self):
        print(len(self.items) == 0)

    def size(self):
        print(len(self.items))
        


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.peek()  # Output: 3
stack.pop()   
stack.pop()   
stack.is_empty()  # Output: False
stack.pop()   # Output: 1
stack.is_empty()  # Output: True
qr3stack.size()