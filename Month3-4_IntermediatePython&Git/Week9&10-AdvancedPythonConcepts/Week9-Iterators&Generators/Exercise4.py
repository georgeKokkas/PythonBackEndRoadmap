# Create a generator expression and iterate through its values.

# Define a generator expression that generates square numbers
gen_exp = (x * x for x in range(5))

# Use the next() function to get the next value from the generator expression
print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1
print(next(gen_exp))  # Output: 4
print(next(gen_exp))  # Output: 9
print(next(gen_exp))  # Output: 16
