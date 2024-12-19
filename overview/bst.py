class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if not self.root:
            self.root = Node(value)  # If tree is empty, set root
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:  # Go to the left subtree
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:  # Go to the right subtree
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)
        # Ignore duplicates (no insertion for duplicate values)

    def search(self, value):
        """Search for a value in the BST. Returns True if found, False otherwise."""
        return self._search(self.root, value)

    def _search(self, current, value):
        if not current:  # Reached a leaf node
            return False
        if current.value == value:
            return True
        elif value < current.value:  # Search in the left subtree
            return self._search(current.left, value)
        else:  # Search in the right subtree
            return self._search(current.right, value)

    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete(self.root, value)

    def _delete(self,  current, value):
        if not current:  # Value not found
            return None

        if value < current.value:  # Go to the left subtree
            current.left = self._delete(current.left, value)
        elif value > current.value:  # Go to the right subtree
            current.right = self._delete(current.right, value)
        else:
            # Node to delete found
            # Case 1: Node with no children
            if not current.left and not current.right:
                return None
            # Case 2: Node with one child
            if not current.left:
                return current.right
            if not current.right:
                return current.left
            
            # Case 3: Node with two children
            # Replace the node's value with the smallest value in the right subtree
            min_larger_node = self._find_min(current.right)
            current.value = min_larger_node.value
            # Delete the inorder successor
            current.right = self._delete(current.right, min_larger_node.value)

        return current

    def _find_min(self, current):
        """Find the node with the smallest value in a subtree."""
        while current.left:
            current = current.left
        return current

    def in_order_traversal(self, node, result=None):
        """In-order traversal: Left -> Root -> Right."""
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)
        return result

    def pre_order_traversal(self, node, result=None):
        """Pre-order traversal: Root -> Left -> Right."""
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    def post_order_traversal(self, node, result=None):
        """Post-order traversal: Left -> Right -> Root."""
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.value)
        return result

# Create an instance of the BST
bst = BST()

# Insert elements into the BST
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# Perform traversals
print("In-Order Traversal:", bst.in_order_traversal(bst.root))
# Expected: [3, 5, 7, 10, 12, 15, 18]

print("Pre-Order Traversal:", bst.pre_order_traversal(bst.root))
# Expected: [10, 5, 3, 7, 15, 12, 18]

print("Post-Order Traversal:", bst.post_order_traversal(bst.root))
# Expected: [3, 7, 5, 12, 18, 15, 10]

# Search for elements
print("Search for 7:", bst.search(7))  # Expected: True
print("Search for 20:", bst.search(20))  # Expected: False

# Delete nodes
bst.delete(3)  # Delete a leaf node
print("In-Order Traversal after deleting 3:", bst.in_order_traversal(bst.root))
# Expected: [5, 7, 10, 12, 15, 18]

bst.delete(15)  # Delete a node with one child
print("In-Order Traversal after deleting 15:", bst.in_order_traversal(bst.root))
# Expected: [5, 7, 10, 12, 18]

bst.delete(10)  # Delete a node with two children (root)
print("In-Order Traversal after deleting 10:", bst.in_order_traversal(bst.root))
# Expected: [5, 7, 12, 18]
