# Create a simple decorator and apply it to a function.

# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Apply the decorator to the function using the '@' symbol
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
