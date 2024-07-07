# Write a function to calculate the factorial of a number.

# Defining a function
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Calling a function
print(factorial(5)) # Output: 120