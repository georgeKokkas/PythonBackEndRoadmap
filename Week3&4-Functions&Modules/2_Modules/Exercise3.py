# Use the 'random' module to generate a list of 10 random numbers between 1 and 100.

import random

random_numbers = [random.randint(1, 100) for n in range(10)]
print(random_numbers) # Output: [76, 13, 1, 58, 10, 93, 87, 2, 34, 35]