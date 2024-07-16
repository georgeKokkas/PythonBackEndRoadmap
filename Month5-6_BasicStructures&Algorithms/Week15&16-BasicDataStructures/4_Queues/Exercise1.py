#  Implement a circular queue and perform operations to add 
# and remove elements.

# Concept: A circular queue is a linear data structure that follows 
# the First In First Out (FIFO) principle, but the last position is 
# connected back to the first position to make a circle.

# Define a class for the Circular Queue
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity  # Set the capacity of the queue
        self.queue = [None] * capacity  # Initialize the queue with None
        self.front = self.rear = -1  # Initialize front and rear pointers

    # Function to add an element to the queue
    def enqueue(self, data):
        if (self.rear + 1) % self.capacity == self.front:
            return "Queue is full"  # Check if the queue is full
        elif self.front == -1:
            self.front = self.rear = 0  # If the queue is empty, initialize front and rear to 0
        else:
            self.rear = (self.rear + 1) % self.capacity  # Increment rear pointer in a circular manner
        self.queue[self.rear] = data  # Add the data to the queue

    # Function to remove an element from the queue
    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"  # Check if the queue is empty
        data = self.queue[self.front]  # Get the data from the front
        if self.front == self.rear:
            self.front = self.rear = -1  # If the queue has only one element, reset front and rear to -1
        else:
            self.front = (self.front + 1) % self.capacity  # Increment front pointer in a circular manner
        return data  # Return the dequeued data

    # Function to print the queue
    def print_queue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.rear >= self.front:
            print(" -> ".join(map(str, self.queue[self.front:self.rear + 1])))
        else:
            print(" -> ".join(map(str, self.queue[self.front:self.capacity] + self.queue[0:self.rear + 1])))

# Create a circular queue and perform operations
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.print_queue()  # Output: 1 -> 2 -> 3 -> 4
cq.dequeue()
cq.print_queue()  # Output: 2 -> 3 -> 4
cq.enqueue(5)
cq.enqueue(6)
cq.print_queue()  # Output: 2 -> 3 -> 4 -> 5 -> 6
print(cq.enqueue(7))  # Output: Queue is full
cq.dequeue()
cq.enqueue(7)
cq.print_queue()  # Output: 3 -> 4 -> 5 -> 6 -> 7
