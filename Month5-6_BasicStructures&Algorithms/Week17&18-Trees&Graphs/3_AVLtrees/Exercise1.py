# Create an AVL tree and implement functions to delete a node.

# Define a class for the Node
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.left = None  # Initialize left child as None
        self.right = None  # Initialize right child as None
        self.height = 1  # Initialize height of the node

# Define a class for the AVL Tree
class AVLTree:
    def __init__(self):
        self.root = None  # Initialize root as None

    # Function to insert a new node in the AVL tree
    def insert(self, data):
        self.root = self._insert(self.root, data)

    # Helper function to insert a new node in the AVL tree
    def _insert(self, node, data):
        if node is None:
            return Node(data)  # Create a new node if the tree is empty

        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        # Update the height of the ancestor node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Get the balance factor
        balance = self._get_balance(node)

        # If the node becomes unbalanced, then perform rotations
        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Function to delete a node in the AVL tree
    def delete(self, data):
        self.root = self._delete(self.root, data)

    # Helper function to delete a node in the AVL tree
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

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # If the node becomes unbalanced, then perform rotations
        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Function to perform right rotation
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return the new root
        return y

    # Function to perform left rotation
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return the new root
        return y

    # Function to get the height of the node
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # Function to get the balance factor of the node
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Function to find the minimum value in the AVL tree
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Function for in-order traversal of the AVL tree
    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    # Helper function for in-order traversal
    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(node.data, end=" ")  # Print the data
            self._in_order_traversal(node.right)

# Create an AVL tree and perform operations
avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)

print("In-order Traversal before deletion:")
avl.in_order_traversal()  # Output: 10 20 25 30 40 50

avl.delete(30)

print("\nIn-order Traversal after deletion:")
avl.in_order_traversal()  # Output: 10 20 25 40 50
