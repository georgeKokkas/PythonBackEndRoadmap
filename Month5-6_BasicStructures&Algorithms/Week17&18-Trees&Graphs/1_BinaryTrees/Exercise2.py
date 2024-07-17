# Write a function to find the height of a binary tree.

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

    # Function to find the height of the binary tree
    def find_height(self):
        return self._find_height(self.root)

    # Helper function to find the height of the binary tree
    def _find_height(self, node):
        if node is None:
            return -1  # Return -1 for empty tree
        left_height = self._find_height(node.left)
        right_height = self._find_height(node.right)
        return 1 + max(left_height, right_height)  # Return the maximum height

# Create a binary tree and find its height
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

print("Height of the Binary Tree:", bt.find_height())  # Output: 2
