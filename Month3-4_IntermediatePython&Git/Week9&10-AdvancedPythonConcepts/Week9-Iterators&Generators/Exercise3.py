# Create a generator function and iterate through its values.

# Define a generator function
def simple_generator():
    yield 1  # Yield returns a value and pauses the function
    yield 2
    yield 3

# Create a generator object by calling the generator function
gen = simple_generator()

# Use the next() function to get the next value from the generator
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
