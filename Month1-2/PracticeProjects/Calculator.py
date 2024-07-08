# Define a function to display the menu and get the user's choice
def display_menu():
    # Prompt the user to choose an arithmetic operation
    operation = input("Choose the arithmetic operation you want to perform (+, -, *, /): ")
    return operation

# Define a function to get two numbers from the user
def get_numbers():
    # Prompt the user to enter the first number
    number1 = float(input("Enter the first number: "))
    # Prompt the user to enter the second number
    number2 = float(input("Enter the second number: "))
    return number1, number2

# Define a function to perform the calculation based on the user's choice
def calculate(operation, number1, number2):
    if operation == "+":
        # Perform addition
        result = number1 + number2
    elif operation == "-":
        # Perform subtraction
        result = number1 - number2
    elif operation == "*":
        # Perform multiplication
        result = number1 * number2
    elif operation == "/":
        # Perform division and handle division by zero
        if number2 == 0:
            result = "Error! Division by zero."
        else:
            result = number1 / number2
    else:
        # Handle invalid operation
        result = "Invalid operation!"
    return result

# Define a function to display the result
def display_result(result):
    # Print the result of the calculation
    print("The result is:", result)

# Main program loop
while True:
    # Display the menu and get the user's choice
    operation = display_menu()
    # Get the numbers from the user
    number1, number2 = get_numbers()
    # Perform the calculation
    result = calculate(operation, number1, number2)
    # Display the result
    display_result(result)
    # Prompt the user to continue or exit
    continue_or_exit = input("Do you want to perform another calculation (c) or exit (e)? ")
    if continue_or_exit.lower() == "e":
        break
    elif continue_or_exit.lower() == "c":
        continue
    else:
        print("Invalid choice! Exiting.")
        break
