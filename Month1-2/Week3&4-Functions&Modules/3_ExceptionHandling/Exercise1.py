# Write a program that asks for user input and catches exceptions if the input is not a number.

try:
    user_input = input("Enter an integer number: ")
    number = int(user_input)
    print(f"You entered: {number}")

except ValueError:
    print("Invalid input! Please enter a valid integer 2number.")