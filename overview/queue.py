class Queue:
    def __init__(self):
        self.Queue = []

    def push(self, item):
        self.Queue.append(item)
    
    def pop(self):
        self.Queue.pop(0)

    def peek(self):
        print(self.Queue[0])

    def isEmpty(self):
       print(len(self.Queue) == 0)

    def size(self):
        print(len(self.Queue))
        

def main():
    queue1 = Queue()
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    queue1.push(4)
    queue1.pop()
    queue1.peek()
    queue1.size()
    queue1.isEmpty()

main() # type: ignore