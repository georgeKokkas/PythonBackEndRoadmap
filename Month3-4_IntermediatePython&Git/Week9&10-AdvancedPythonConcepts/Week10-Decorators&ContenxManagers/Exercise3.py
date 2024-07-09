# Create a custom context manager class and use it with with statement.

# Define a custom context manager class
class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self  # Return the context manager object

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")
        # exc_type, exc_value, and traceback are used to handle exceptions if any

# Use the custom context manager with the 'with' statement
with MyContextManager() as manager:
    print("Inside the context.")
# Output:
# Entering the context.
# Inside the context.
# Exiting the context.
