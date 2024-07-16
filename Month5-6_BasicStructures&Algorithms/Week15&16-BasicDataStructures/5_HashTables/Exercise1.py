# Implement a hash table with collision handling using chaining (linked lists).

# Define a class for the Node
class Node:
    def __init__(self, key, value):
        self.key = key  # Store key
        self.value = value  # Store value
        self.next = None  # Initialize next as None

# Define a class for the Hash Table
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Set the capacity of the hash table
        self.table = [None] * capacity  # Initialize the table with None

    # Function to compute the hash value of a key
    def hash(self, key):
        return hash(key) % self.capacity  # Compute the hash value

    # Function to add a key-value pair to the hash table
    def set_item(self, key, value):
        index = self.hash(key)  # Get the index for the key
        if self.table[index] is None:
            self.table[index] = Node(key, value)  # Create a new node if the index is empty
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value  # Update the value if the key already exists
                    return
                current = current.next
            if current.key == key:
                current.value = value  # Update the value if the key already exists
            else:
                current.next = Node(key, value)  # Add a new node at the end of the linked list

    # Function to get a value by key from the hash table
    def get_item(self, key):
        index = self.hash(key)  # Get the index for the key
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value  # Return the value if the key is found
            current = current.next
        return "Key not found"

    # Function to remove a key-value pair from the hash table
    def remove_item(self, key):
        index = self.hash(key)  # Get the index for the key
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next  # Remove the node if it's not the first node
                else:
                    self.table[index] = current.next  # Remove the node if it's the first node
                return
            prev = current
            current = current.next
        print("Key not found")

    # Function to display the hash table
    def display(self):
        for i in range(self.capacity):
            print(f"Bucket {i}:", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")

# Create a hash table and perform operations
ht = HashTable(5)
ht.set_item("name", "Alice")
ht.set_item("age", 25)
ht.set_item("city", "New York")
ht.display()
print(ht.get_item("name"))  # Output: Alice
print(ht.get_item("age"))   # Output: 25
ht.remove_item("city")
ht.display()  # Bucket 0: None
