class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedLists:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:  # If the list is empty
            self.head = new_node
            return

        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next

        current.next = new_node  # Link the last node to the new node
        new_node.prev = current  # Link the new node back to the last node

    def printDLL(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")  # Indicate the end of the list

    def remove(self, element):
    # Check if the list is empty
        if not self.head:
            print("List is empty. Nothing to remove.")
            return

        current = self.head

        # Case 1: Remove the head node
        if current.value == element:
            self.head = current.next
            if self.head:  # Update the new head's prev pointer if the list is not empty now
                self.head.prev = None
            return

        # Case 2: Traverse to find the node to remove
        while current and current.value != element:
            current = current.next

        # If the element is not found
        if not current:
            print("Element not found.")
            return

        # Case 3: Remove a middle or tail node
        if current.next:  # If it is not the last node
            current.next.prev = current.prev

        if current.prev:  # If it is not the head node
            current.prev.next = current.next

    def add(self, position, value):
        new_node = Node(value)

        # Case 1: Adding to an empty list
        if not self.head:
            if position == 0:
                self.head = new_node
                return
            else:
                print("Invalid position for an empty list.")
                return

        # Case 2: Adding at the head of the list
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # Case 3: Adding in the middle or end of the list
        current = self.head
        inc = 0

        # Traverse to the (position - 1) node
        while current and inc != position - 1:
            current = current.next
            inc += 1

        # If the position is invalid (e.g., too large)
        if not current:
            print("Position out of bounds.")
            return

        new_node.next = current.next #current next->  now is also new node next->  (both pointing to next)
        current.next.prev = new_node #Current -> new node <-prev next 
        new_node.prev = current # current <-prev new node
        current.next = new_node# current next-> new node 


        
        




def main():
    ddl = DoublyLinkedLists()
    ddl.append(1)
    ddl.append(2)
    ddl.append(3)
    ddl.append(4)
    ddl.remove(3)
    ddl.add(1, 5)
    ddl.printDLL()  

main()
