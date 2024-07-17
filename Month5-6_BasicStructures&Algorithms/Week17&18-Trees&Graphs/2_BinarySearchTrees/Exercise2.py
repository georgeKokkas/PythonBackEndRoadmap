# Write a function to find the minimum and maximum values 
# in a binary search tree.

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

    # Function to find the minimum value in the binary search tree
    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    # Function to find the maximum value in the binary search tree
    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

# Create a binary search tree and find the minimum and maximum values
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Minimum value in the Binary Search Tree:", bst.find_min())  # Output: 2
print("Maximum value in the Binary Search Tree:", bst.find_max())  # Output: 8
