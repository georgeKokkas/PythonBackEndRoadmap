# Implement a doubly linked list and perform operations to add and 
# remove elements from both ends.

# Define a class for the Node
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize next as None
        self.prev = None  # Initialize prev as None

# Define a class for the Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    # Function to add a new node at the end
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse to the last node
        last.next = new_node  # Make the last node point to the new node
        new_node.prev = last  # Make the new node's prev point to the last node

    # Function to add a new node at the beginning
    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        self.head.prev = new_node  # Make the current head's prev point to the new node
        new_node.next = self.head  # Make the new node's next point to the current head
        self.head = new_node  # Make the new node the head

    # Function to remove a node from the end
    def remove_end(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None  # If the list has only one node, make head None
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse to the last node
        last.prev.next = None  # Make the second last node's next None

    # Function to remove a node from the beginning
    def remove_beginning(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None  # If the list has only one node, make head None
            return
        self.head = self.head.next  # Make the second node the head
        self.head.prev = None  # Make the new head's prev None

    # Function to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")  # Print the data
            current = current.next
        print("None")  # Indicate the end of the list

# Create a doubly linked list and perform operations
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.print_list()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> None
dll.remove_end()
dll.print_list()  # Output: 0 <-> 1 <-> 2 <-> None
dll.remove_beginning()
dll.print_list()  # Output: 1 <-> 2 <-> None
