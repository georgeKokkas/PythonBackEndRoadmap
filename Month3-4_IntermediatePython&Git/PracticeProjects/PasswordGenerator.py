# This will be a simple password generator. 
# This project will allow users to generate random passwords 
# based on specified criteria such as length, inclusion of uppercase letters, 
# numbers, and special characters.

# A simple password generator should:

#     Allow the user to specify the desired length of the password.
#     Allow the user to choose whether to include uppercase letters, numbers, and special characters.
#     Generate a random password based on the user's specifications.
#     Display the generated password.

# Import the 'random' module to generate random characters
import random

# Import the 'string' module to access character sets
import string


# Define the character sets
lowercase_letters = string.ascii_lowercase
# 'string.ascii_lowercase' gives all lowercase letters: 'abcdefghijklmnopqrstuvwxyz'

uppercase_letters = string.ascii_uppercase
# 'string.ascii_uppercase' gives all uppercase letters: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers = string.digits
# 'string.digits' gives all digits: '0123456789'

special_characters = string.punctuation
# 'string.punctuation' gives all special characters: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


# Define a function to get the user's preferences for the password
def get_user_preferences():
    # Get the desired length of the password from the user
    length = int(input("Enter the desired length of the password: "))

    # Ask the user if they want to include uppercase letters
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'

    # Ask the user if they want to include numbers
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'

    # Ask the user if they want to include special characters
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Return the user's preferences as a tuple
    return length, include_uppercase, include_numbers, include_special


# Define a function to generate a password based on the user's preferences
def generate_password(length, include_uppercase, include_numbers, include_special):
    # Start with the lowercase letters
    character_set = lowercase_letters

    # Add uppercase letters if the user wants them
    if include_uppercase:
        character_set += uppercase_letters

    # Add numbers if the user wants them
    if include_numbers:
        character_set += numbers

    # Add special characters if the user wants them
    if include_special:
        character_set += special_characters

    # Generate the password by randomly choosing characters from the character set
    password = ''.join(random.choice(character_set) for _ in range(length))

    # Return the generated password
    return password


# Define a function to display the generated password
def display_password(password):
    print(f"Generated password: {password}")


def main():
    while True:
        # Get the user's preferences
        length, include_uppercase, include_numbers, include_special = get_user_preferences()

        # Generate the password based on the user's preferences
        password = generate_password(length, include_uppercase, include_numbers, include_special)

        # Display the generated password
        display_password(password)

        # Ask the user if they want to generate another password or exit
        continue_or_exit = input("Do you want to generate another password? (yes/no): ").lower()
        if continue_or_exit != 'yes':
            print("Exiting the password generator.")
            break

# Call the main function to start the program
if __name__ == "__main__":
    main()