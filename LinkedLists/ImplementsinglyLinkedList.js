class Node{
    constructor(val, next){
        this.val = val
        this.next = next
    }
}

class SinglyLinkedList{
    constructor (val, next){
        this.head = {
            val: val,
            next: null
        }
        this.tail = this.head
        this.len = 1
    }

    append(val){
        let newNode = new Node(val)
        this.head.next = newNode
        this.tail = newNode
        this.len++;
    }

    transverse(){
    }

}

function main(){
    linkedList = new SinglyLinkedList(10);
    linkedList.append(20);

}

main()