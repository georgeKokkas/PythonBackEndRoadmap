# Implement a stack using a linked list instead of a list.

# A stack can be implemented using a linked list where the top 
# of the stack is represented by the head of the linked list.

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

    # Function to print the stack
    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print the data
            current = current.next
        print("None")  # Indicate the end of the stack

# Create a stack and perform operations
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()  # Output: 3 -> 2 -> 1 -> None
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
stack.print_stack()  # Output: 2 -> 1 -> None
print(stack.is_empty())  # Output: False
