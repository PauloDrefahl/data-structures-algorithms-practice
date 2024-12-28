#implementing linked lists in python.

class Node:

    def __init__(self, value): 
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def transverse(self):
        current = self.head
        while current:
            print(current.value, end="->")
            current = current.next

    def delete(self, value):
        if not self.head:
            return
        
        current = self.head

        if current == value:
            self.head == self.head.next
            return 

        while current.next and current.next.value != value:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            return

        print("value not found")

    def preend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add(self, position, value):
        new_node = Node(value)
        current = self.head
        inc = 0

        # Traverse the list to the node before the target position
        while current and inc < position - 1:
            inc += 1
            current = current.next

        # If `current` is None, the position is out of range
        if not current:
            print("Position out of range")
            return

        # Insert the new node
        new_node.next = current.next
        current.next = new_node
            
    
        
 
        
def main():
    list1 = LinkedList()
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    list1.delete(4)
    list1.preend(1)
    list1.add(3, 4)
    list1.transverse()
    
main()

class Car:
    def __init__(self, model):
        self.model = model
    
    def sound():
        print("sound")

class Honda : Car