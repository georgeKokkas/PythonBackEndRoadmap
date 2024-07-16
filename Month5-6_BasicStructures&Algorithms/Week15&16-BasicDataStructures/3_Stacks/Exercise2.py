# Write a function to check for balanced parentheses in an expression
# using a stack.

# Define a class for the Node
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize next as None

# Define a class for the Stack
class Stack:
    def __init__(self):
        self.head = None  # Initialize head as None

    # Function to add an element to the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Make the new node point to the current head
        self.head = new_node  # Make the new node the head

    # Function to remove the top element from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.head  # Store the current head
        self.head = self.head.next  # Make the next node the new head
        return popped_node.data  # Return the data of the popped node

    # Function to check if the stack is empty
    def is_empty(self):
        return self.head is None  # Return True if the head is None, else False

    # Function to view the top element of the stack
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.data  # Return the data of the head

# Define a function to check for balanced parentheses in an expression
def is_balanced(expression):
    stack = Stack()
    # Dictionary to hold matching pairs of parentheses
    matching_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in matching_pairs.values():
            stack.push(char)  # Push opening parentheses to the stack
        elif char in matching_pairs.keys():
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return False  # Return False if there is no matching opening parenthesis
    return stack.is_empty()  # Return True if the stack is empty

# Test the function
expression = "({[()]})"
print(is_balanced(expression))  # Output: True

expression = "({[([)])})"
print(is_balanced(expression))  # Output: False
