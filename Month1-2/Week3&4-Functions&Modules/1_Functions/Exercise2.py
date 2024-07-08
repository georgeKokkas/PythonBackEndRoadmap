# Create a function that accepts a list of numbers and returns a new list with only the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Defining a function to get a new list of even numbers
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0] # Return a new list created using a list comprehension

# Calling the function
print(get_even_numbers(numbers)) # Output: [2, 4, 6, 8, 10]