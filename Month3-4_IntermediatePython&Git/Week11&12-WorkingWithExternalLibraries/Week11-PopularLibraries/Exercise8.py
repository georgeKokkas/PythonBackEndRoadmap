# Perform element-wise operations on two arrays and print the results.

# Import the 'numpy' library to handle numerical operations
import numpy as np

# Create two arrays of random numbers
array1 = [np.random.randint(1, 10) for n in range(5)]
array2 = [np.random.randint(1, 10) for n in range(5)]

# Print the arrays
print("Array 1:", array1)
print("Array 2:", array2)

# Perform element-wise addition
addition = np.add(array1, array2)
print("Addition:", addition)

# Perform element-wise subtraction
subtraction = np.subtract(array1, array2)
print("Subtraction:", subtraction)

# Perform element-wise multiplication
multiplication = np.multiply(array1, array2)
print("Multiplication:", multiplication)

# Perform element-wise division
division = np.divide(array1, array2)
print("Division:", division)
