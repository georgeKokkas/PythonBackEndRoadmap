# Write a function to reverse a singly linked list.

# Define a class for the Node
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize next as None

# Define a class for the Singly Linked List
class SinglyLinkedList:
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

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move the prev pointer one step forward
            current = next_node  # Move the current pointer one step forward
        self.head = prev  # Update the head to be the new front

    # Function to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print the data
            current = current.next
        print("None")  # Indicate the end of the list

# Create a singly linked list and perform operations
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list()  # Output: 1 -> 2 -> 3 -> None
sll.reverse()
sll.print_list()  # Output: 3 -> 2 -> 1 -> None
