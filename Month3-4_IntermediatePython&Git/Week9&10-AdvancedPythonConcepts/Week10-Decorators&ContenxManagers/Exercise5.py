# Use the re module to find all words in a string that start with a specific letter.

# Import the re module for working with regular expressions
import re

# Define a pattern to match words that start with 'a'
pattern = r"\ba\w*"

# Use the re.findall function to find all matches in the string
matches = re.findall(pattern, "an apple a day keeps the doctor away.")
print(matches)  # Output: ['an', 'apple', 'a', 'away']
