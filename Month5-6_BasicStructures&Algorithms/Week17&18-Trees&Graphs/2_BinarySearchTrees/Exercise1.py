# Create a binary search tree and implement functions to delete a node.

# Define a class for the Node
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.left = None  # Initialize left child as None
        self.right = None  # Initialize right child as None

# Define a class for the Binary Search Tree
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize root as None

    # Function to insert a new node in the binary search tree
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)  # If the tree is empty, make the new node the root
        else:
            self._insert(self.root, data)

    # Helper function to insert a new node in the binary search tree
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)  # Insert as left child if empty
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)  # Insert as right child if empty
            else:
                self._insert(node.right, data)

    # Function to delete a node in the binary search tree
    def delete(self, data):
        self.root = self._delete(self.root, data)

    # Helper function to delete a node in the binary search tree
    def _delete(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    # Function to find the minimum value in the binary search tree
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Function for in-order traversal of the binary search tree
    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    # Helper function for in-order traversal
    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(node.data, end=" ")  # Print the data
            self._in_order_traversal(node.right)

# Create a binary search tree and perform operations
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("In-order Traversal before deletion:")
bst.in_order_traversal()  # Output: 2 3 4 5 6 7 8

bst.delete(3)

print("\nIn-order Traversal after deletion:")
bst.in_order_traversal()  # Output: 2 4 5 6 7 8
