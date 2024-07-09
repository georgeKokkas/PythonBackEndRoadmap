# Use the re module to replace all digits in a string with a specific character.

# Import the re module for working with regular expressions
import re

# Define a pattern to match digits
pattern = r"\d"

# Use the re.sub function to replace all digits with 'X'
result = re.sub(pattern, "X", "There are 2 apples, 3 bananas, and 5 oranges.")
print(result)  # Output: There are X apples, X bananas, and X oranges.
