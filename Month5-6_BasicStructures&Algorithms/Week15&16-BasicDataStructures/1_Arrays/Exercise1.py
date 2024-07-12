# Create an array of floats and perform operations to access, 
# modify, add, and remove elements.

# Import the array module from the standard library
import array

# Create an array of floats
arr = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
# 'f' is the type code for float array, [1.1, 2.2, 3.3, 4.4, 5.5] are the initial values

# Access elements in the array
print(arr[0])  # Output: 1.1
print(arr[2])  # Output: 3.3

# Modify an element in the array
arr[1] = 20.2
print(arr)  # Output: array('f', [1.1, 20.2, 3.3, 4.4, 5.5])

# Add an element to the array
arr.append(6.6)
print(arr)  # Output: array('f', [1.1, 20.2, 3.3, 4.4, 5.5, 6.6])

# Function to remove an element from the array with a tolerance for floating-point comparison
def remove_float(arr, value, tolerance=1e-5):
    index_to_remove = -1 # Initializes the index to remove to -1, indicating that no element has been found yet
    for i in range(len(arr)): #  Iterates through the array
        if abs(arr[i] - value) < tolerance: # Checks if the absolute difference between the current element and the value is less than the tolerance
            index_to_remove = i # Sets the index to remove to the current index
            break # Breaks the loop once the element is found
    if index_to_remove != -1: #  Checks if an element to remove was found
        arr.pop(index_to_remove) # Removes the element at the specified index

# Remove an element from the array
remove_float(arr, 3.3)
print(arr)  # Output: array('f', [1.1, 20.2, 4.4, 5.5, 6.6])
