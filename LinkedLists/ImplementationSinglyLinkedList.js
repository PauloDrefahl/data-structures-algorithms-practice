class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

class SinglyLinkedList {
    constructor(value){

        this.head = {
        value: value,
        next: null
        }

        this.tail = this.head;
        this.length = 1;
    } 

    append(value){
        let newNode = new Node(value)
        this.tail.next = newNode 
        this.tail = newNode
        this.length++
    }

}

const LinkedList = new SinglyLinkedList(10);
LinkedList.append(15);
LinkedList.append(20);


console.log(LinkedList)

//we need an append method that will add to the linked list.

