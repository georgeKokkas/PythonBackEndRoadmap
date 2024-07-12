# Write a function to find the maximum and minimum values in the array

# Import the array module from the standard library
import array

# Define a function to find the maximum and minimum values in the array
def find_max_min(arr):
    # Initialize max and min with the first element of the array
    max_value = arr[0]
    min_value = arr[0]
    
    # Iterate through the array to find the max and min values
    for num in arr:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    return max_value, min_value

# Create an array of floats
arr = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])

# Call the function and print the result
max_value, min_value = find_max_min(arr)
print(f"Maximum value: {max_value}")  # Output: Maximum value: 5.5
print(f"Minimum value: {min_value}")  # Output: Minimum value: 1.1
