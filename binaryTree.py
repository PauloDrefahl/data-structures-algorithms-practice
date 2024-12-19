class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertRecursively(self, current, value):
        if value < current.value: #if the value is less than the current value passed
            if current.left is None: #if left value is not there
                current.left = Node(value)
            else:
                self.insertRecursively(current.left, value)
        
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insertRecursively(current.right, value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insertRecursively(self.root, value)

    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)  # Visit left
            result.append(node.value)  # Visit root
            self.in_order_traversal(node.right, result)  # Visit right
        return result
    
    def pre_order_traversal(self, node, result=None):
        if not result:
            result = []
        if node:
            result.append(node.value)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right,result)
        return result
    
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left,result)
            self.post_order_traversal(node.right, result)
            result.append(node.value)
        return result
    

# Create an instance of BinaryTree
bt = BinaryTree()



# Insert values into the binary tree
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(18)


# Perform and print results of different traversals
print("In-Order Traversal:", bt.in_order_traversal(bt.root))
# Expected Output: [3, 5, 7, 10, 12, 15, 18]

print("Pre-Order Traversal:", bt.pre_order_traversal(bt.root))
# Expected Output: [10, 5, 3, 7, 15, 12, 18]

print("Post-Order Traversal:", bt.post_order_traversal(bt.root))
# Expected Output: [3, 7, 5, 12, 18, 15, 10]
