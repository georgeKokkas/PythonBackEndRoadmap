# Write a function to count the frequency of each character 
# in a string using a hash table.

# Define a function to count the frequency of each character in a string
def count_char_frequency(string):
    # Initialize an empty dictionary to represent the hash table
    hash_table = {}

    # Iterate through each character in the string
    for char in string:
        # If the character is already in the hash table, increment its count
        if char in hash_table:
            hash_table[char] += 1
        else:
            # Otherwise, add the character to the hash table with a count of 1
            hash_table[char] = 1

    # Return the hash table
    return hash_table

# Test the function
string = "hello world"
frequency = count_char_frequency(string)
print(frequency)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
