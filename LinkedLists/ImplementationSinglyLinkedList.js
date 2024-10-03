class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor(value) {
        if (value !== undefined) {
            this.head = new Node(value);
            this.tail = this.head;
            this.length = 1;
        } else {
            this.head = null;
            this.tail = null;
            this.length = 0;
        }
    }

    // Append: Add node at the end
    append(value) {
        const newNode = new Node(value);
        if (!this.head) {
            this.head = newNode;
            this.tail = this.head;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
    }

    // Prepend: Add node at the beginning
    prepend(value) {
        const newNode = new Node(value);
        if (!this.head) {
            this.head = newNode;
            this.tail = this.head;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
    }

    // Insert at a specific index
    insert(index, value) {
        if (index >= this.length) {
            this.append(value); // If out of bounds, append at the end
            return;
        }
        if (index === 0) {
            this.prepend(value);
            return;
        }
        const newNode = new Node(value);
        let prev = this.traverseToIndex(index - 1);
        newNode.next = prev.next;
        prev.next = newNode;
        this.length++;
    }

    // Remove a node from a specific index
    remove(index) {
        if (index < 0 || index >= this.length) {
            return null;
        }
        if (index === 0) {
            this.head = this.head.next;
            this.length--;
            return;
        }
        const prev = this.traverseToIndex(index - 1);
        const nodeToRemove = prev.next;
        prev.next = nodeToRemove.next;
        if (index === this.length - 1) {
            this.tail = prev; // Update tail if last element is removed
        }
        this.length--;
    }

    // Traverse to a specific index
    traverseToIndex(index) {
        let currentNode = this.head;
        let counter = 0;
        while (counter !== index) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }

    // Find a node with specific value
    find(value) {
        let currentNode = this.head;
        while (currentNode) {
            if (currentNode.value === value) {
                return currentNode;
            }
            currentNode = currentNode.next;
        }
        return null; // Return null if value is not found
    }

    // Convert Linked List to Array (for easier display)
    toArray() {
        const array = [];
        let currentNode = this.head;
        while (currentNode) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }

    // Print the list
    printList() {
        console.log(this.toArray());
    }
}

// Testing the enhanced SinglyLinkedList
const linkedList = new SinglyLinkedList();
linkedList.append(10);
linkedList.append(15);
linkedList.append(20);
linkedList.prepend(5);     // Add 5 at the beginning
linkedList.insert(2, 12);  // Insert 12 at index 2
linkedList.remove(3);      // Remove the node at index 3 (15 will be removed)
linkedList.printList();     // Output: [5, 10, 12, 20]

console.log('Found:', linkedList.find(20));  // Find and log node with value 20
console.log('List as Array:', linkedList.toArray());  // Convert and display as array
