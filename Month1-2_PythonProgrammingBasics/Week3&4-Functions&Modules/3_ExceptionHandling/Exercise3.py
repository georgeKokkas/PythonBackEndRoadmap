# Implement a custom exception for a function that checks if a string is a palindrome.

# Define a custom exception class named 'NotAPalindromeError' that inherits from the built-in 'Exception' class
class NotAPalindromeError(Exception):
    # Use 'pass' to indicate that there is no additional functionality to add to this custom exception class
    pass

# Define a function named 'check_palindrome' that takes one parameter 's' (a string)
def check_palindrome(s):
    # Check if the string 's' is not equal to its reverse
    if s != s[::-1]:
        # If the string is not a palindrome, raise the custom exception 'NotAPalindromeError'
        # Include a message that indicates the string is not a palindrome
        raise NotAPalindromeError(f"'{s}' is not a palindrome!")
    # If the string is a palindrome, return a message that indicates the string is indeed a palindrome
    return f"'{s}' is indeed a palindrome!"

# Use a try/except block to handle exceptions that may be raised
try:
    # Call the 'check_palindrome' function with the string "radar" and print the result
    print(check_palindrome("radar"))  # Output: True
    # Call the 'check_palindrome' function with the string "hello" and print the result
    # This will raise the 'NotAPalindromeError' exception because "hello" is not a palindrome
    print(check_palindrome("hello"))
# Catch the 'NotAPalindromeError' exception and assign it to the variable 'e'
except NotAPalindromeError as e:
    # Print the exception message
    print(e)  # Output: 'hello' is not a palindrome!
