# Implement a recursive function to calculate the power of a number.

# Concept: Recursion is a method where the solution to a problem depends on 
# solutions to smaller instances of the same problem. A recursive function 
# calls itself to break down the problem into smaller sub-problems.

def power(base, exponent):
    # Base case: any number to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: multiply the base by the result of the base to the power of exponent-1
    else:
        return base * power(base, exponent - 1)

# Test Power Function
print("2^3:", power(2, 3))  # Output: 8
print("5^4:", power(5, 4))  # Output: 625
