# Create an iterator from a list and print each item using next().

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Get an iterator from the list using the iter() function
iterator = iter(numbers)

# Use the next() function to get the next item from the iterator
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
print(next(iterator))  # Output: 5
# next() retrieves the next element from the iterator until there are no more elements
