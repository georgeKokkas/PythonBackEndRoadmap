# Write a dictionary comprehension to create a dictionary mapping numbers to their cubes for the first 5 numbers.

# Create a dictionary mapping numbers to their cubes using a dictionary comprehension
cubes = {x: x**3 for x in range(5)}

# Print the dictionary of cubes
print(cubes)
# Output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
