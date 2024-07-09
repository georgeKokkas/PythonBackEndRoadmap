# Create a custom iterator class.

# Define a custom iterator class
class MyIterator:
    def __init__(self, start, end):
        self.current = start  # Initialize the current value
        self.end = end        # Initialize the end value

    def __iter__(self):
        return self           # Return the iterator object itself

    def __next__(self):
        if self.current > self.end:
            raise StopIteration  # Raise StopIteration when the iteration is complete
        else:
            self.current += 1     # Increment the current value
            return self.current - 1  # Return the current value before incrementing

# Create an instance of the custom iterator
iterator = MyIterator(1, 5)

# Use a for loop to iterate through the custom iterator
for num in iterator:
    print(num)  # Output: 1, 2, 3, 4, 5
