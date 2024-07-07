# Write a program to read a file and count the number of lines, words, and characters.

def count_file_stats(filename):
    # Define a function named 'count_file_stats' that takes one parameter 'filename'
    try:
        # Try to execute the following block of code
        with open(filename, 'r') as file:
            # Open the file with the name 'filename' in read mode ('r')
            # Use 'with' to ensure the file is properly closed after reading
            lines = file.readlines()
            # Read all the lines from the file and store them in the 'lines' variable

            num_lines = len(lines)
            # Count the number of lines by getting the length of the 'lines' list

            num_words = sum(len(line.split()) for line in lines)
            # Count the total number of words by splitting each line into words and summing the lengths

            num_chars = sum(len(line) for line in lines)
            # Count the total number of characters by summing the length of each line

        return num_lines, num_words, num_chars
        # Return the counts of lines, words, and characters as a tuple

    except FileNotFoundError:
        # If the file is not found, handle the exception
        return "File not found!"
        # Return a message indicating the file was not found


# Define the exact path to the 'example2.txt' file
file_path = "C:/Users/geoko/Desktop/PythonBackEndRoadmap/Week5&6-DataStructures&OOP/3_WorkingWithFiles/example2.txt"

# Call the 'count_file_stats' function with the exact file path
result = count_file_stats(file_path)

# Check if the result is a string (indicating an error)
if isinstance(result, str):
    # If the result is a string, print the error message
    print(result)
else:
    # If the result is not a string, unpack the values into 'lines', 'words', and 'chars'
    lines, words, chars = result
    # Print the counts of lines, words, and characters
    print(f"Lines: {lines}, Words: {words}, Characters: {chars}")
