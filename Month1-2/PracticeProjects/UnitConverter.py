# This converter will allow users to convert between different units 
# of measurement such as length, weight, and temperature.

#     A unit converter should:

#     Display a menu with options for different types of conversions (e.g., length, weight, temperature).
#     Allow the user to select a type of conversion.
#     Prompt the user to enter the value and the units they want to convert from and to.
#     Perform the conversion.
#     Display the result.
#     Allow the user to perform another conversion or exit.

# Define a function to display the menu and get the user's choice
def display_menu():
    print("Select the type of conversion you want to perform:")
    print("1. Length (m to km, km to m)")
    print("2. Weight (g to kg, kg to g)")
    print("3. Temperature (C to F, F to C)")
    choice = input("Enter your choice (1/2/3): ")
    return choice

# Define a function to get the details of the conversion from the user
def get_conversion_details():
    value = float(input("Enter the value to convert: "))
    from_unit = input("Enter the unit to convert from: ")
    to_unit = input("Enter the unit to convert to: ")
    return value, from_unit, to_unit

# Define a function to perform the conversion
def convert(value, from_unit, to_unit):
    if from_unit == "m" and to_unit == "km":
        return value / 1000
    elif from_unit == "km" and to_unit == "m":
        return value * 1000
    elif from_unit == "g" and to_unit == "kg":
        return value / 1000
    elif from_unit == "kg" and to_unit == "g":
        return value * 1000
    elif from_unit == "c" and to_unit == "f":
        return (value * 9/5) + 32
    elif from_unit == "f" and to_unit == "c":
        return (value - 32) * 5/9
    else:
        return "Invalid conversion units!"

# Define a function to display the result of the conversion
def display_result(value, from_unit, converted_value, to_unit):
    print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")

# Main program loop
while True:
    # Display the menu and get the user's choice
    choice = display_menu()
    
    # Get the conversion details from the user
    value, from_unit, to_unit = get_conversion_details()
    
    # Perform the conversion
    converted_value = convert(value, from_unit, to_unit)
    
    # Display the result
    display_result(value, from_unit, converted_value, to_unit)
    
    # Ask the user if they want to perform another conversion or exit
    continue_or_exit = input("Do you want to perform another conversion (yes/no)? ").lower()
    # Check if the user wants to exit
    if continue_or_exit != 'yes':
        break