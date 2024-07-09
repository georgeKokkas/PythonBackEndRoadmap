# Create a decorator that accepts arguments.

# Define a decorator that accepts arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)  # Call the original function multiple times
        return wrapper
    return decorator_repeat

# Apply the decorator to the function with an argument
@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("George")
# Output:
# Hello, George!
# Hello, George!
# Hello, George!