# Write a function to simulate a print queue where jobs 
# are processed in the order they arrive.

# Import the deque class from the collections module
from collections import deque

# Define a class for the Print Queue
class PrintQueue:
    def __init__(self):
        self.queue = deque()  # Initialize an empty deque to represent the print queue

    # Function to add a print job to the queue
    def add_job(self, job):
        self.queue.append(job)  # Append the job to the end of the deque

    # Function to process the next print job
    def process_job(self):
        if self.queue:
            job = self.queue.popleft()  # Remove and return the first job in the deque
            print(f"Processing job: {job}")
        else:
            print("No jobs in the queue")

    # Function to print the queue
    def print_queue(self):
        print("Print Queue:", " -> ".join(self.queue) if self.queue else "Empty")

# Create a print queue and perform operations
pq = PrintQueue()
pq.add_job("Job1")
pq.add_job("Job2")
pq.add_job("Job3")
pq.print_queue()  # Output: Print Queue: Job1 -> Job2 -> Job3
pq.process_job()  # Output: Processing job: Job1
pq.print_queue()  # Output: Print Queue: Job2 -> Job3
pq.process_job()  # Output: Processing job: Job2
pq.print_queue()  # Output: Print Queue: Job3
pq.process_job()  # Output: Processing job: Job3
pq.print_queue()  # Output: Print Queue: Empty
pq.process_job()  # Output: No jobs in the queue
