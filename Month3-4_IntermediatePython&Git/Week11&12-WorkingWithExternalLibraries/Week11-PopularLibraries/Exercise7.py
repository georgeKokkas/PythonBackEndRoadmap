# Create an array of random numbers and calculate the sum, mean, and standard deviation.

# Import the 'numpy' library to handle numerical operations
import numpy as np

# Create an array of 10 random numbers between 1 and 10
random_numbers = [np.random.randint(1, 10) for n in range(10)]

# Print the array of random numbers
print("Random Numbers:", random_numbers)

# Calculate the sum of the array elements
sum_numbers = np.sum(random_numbers)
print(f"Sum: {sum_numbers}")

# Calculate the mean of the array elements
mean_numbers = np.mean(random_numbers)
print(f"Mean: {mean_numbers}")

# Calculate the standard deviation of the array elements
std_numbers = np.std(random_numbers)
print(f"Standard Deviation: {std_numbers}")
