# Create a binary tree and implement pre-order, in-order, 
# and post-order traversal.

# Define a class for the Node
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.left = None  # Initialize left child as None
        self.right = None  # Initialize right child as None

# Define a class for the Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None  # Initialize root as None

    # Function to insert a new node in the binary tree
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)  # If the tree is empty, make the new node the root
        else:
            self._insert(self.root, data)

    # Helper function to insert a new node in the binary tree
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

    # Function for pre-order traversal of the binary tree
    def pre_order_traversal(self):
        self._pre_order_traversal(self.root)

    # Helper function for pre-order traversal
    def _pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")  # Print the data
            self._pre_order_traversal(node.left)
            self._pre_order_traversal(node.right)

    # Function for in-order traversal of the binary tree
    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    # Helper function for in-order traversal
    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(node.data, end=" ")  # Print the data
            self._in_order_traversal(node.right)

    # Function for post-order traversal of the binary tree
    def post_order_traversal(self):
        self._post_order_traversal(self.root)

    # Helper function for post-order traversal
    def _post_order_traversal(self, node):
        if node:
            self._post_order_traversal(node.left)
            self._post_order_traversal(node.right)
            print(node.data, end=" ")  # Print the data

# Create a binary tree and perform operations
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

print("Pre-order Traversal:")
bt.pre_order_traversal()  # Output: 5 3 2 4 7 6 8

print("\nIn-order Traversal:")
bt.in_order_traversal()  # Output: 2 3 4 5 6 7 8

print("\nPost-order Traversal:")
bt.post_order_traversal()  # Output: 2 4 3 6 8 7 5
