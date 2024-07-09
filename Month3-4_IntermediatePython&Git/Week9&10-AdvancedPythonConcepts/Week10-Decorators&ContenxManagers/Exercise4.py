# Create a context manager using the contextlib module.

# Import the contextmanager decorator from the contextlib module
from contextlib import contextmanager

# Define a context manager function using the contextmanager decorator
@contextmanager
def my_context_manager():
    print("Entering the context.")
    yield  # Yield control back to the with statement block
    print("Exiting the context.")

# Use the context manager with the 'with' statement
with my_context_manager():
    print("Inside the context.")
# Output:
# Entering the context.
# Inside the context.
# Exiting the context.