# This will be a simple command-line game where the computer randomly selects 
# a number within a range, and the user has to guess the number. 
# The game will provide hints whether the guess is too high or too low.

#     A number guessing game should:

#     Randomly select a number within a given range.
#     Prompt the user to guess the number.
#     Provide feedback if the guess is too high, too low, or correct.
#     Keep track of the number of guesses.
#     Allow the user to play again or exit.

# Import the 'random' module to generate random numbers
import random

# Define a function to generate a random number within a given range
def generate_random_number(start, end):
    # Use random.randint to generate a random number between 'start' and 'end' (inclusive)
    random_number = random.randint(start, end)
    return random_number

# Define a function to get the user's guess
def get_user_guess():
    # Prompt the user to enter their guess
    guess = int(input("Enter your guess: "))
    return guess

# Define a function to compare the user's guess with the random number
def compare_guess(guess, random_number):
    # Check if the guess is too low
    if guess < random_number:
        print("Your guess is too low.")
        return False
    # Check if the guess is too high
    elif guess > random_number:
        print("Your guess is too high.")
        return False
    # If the guess is correct
    else:
        print("Congratulations! You've guessed the correct number.")
        return True

# Main game loop
def play_game():
    # Define the range for the random number
    start = 1
    end = 10
    
    # Generate a random number within the specified range
    random_number = generate_random_number(start, end)
    
    # Initialize the number of guesses
    number_of_guesses = 0
    
    # Initialize a variable to track if the user has guessed correctly
    guessed_correctly = False
    
    # Loop until the user guesses the correct number
    while not guessed_correctly:
        # Get the user's guess
        guess = get_user_guess()
        
        # Increment the number of guesses
        number_of_guesses += 1
        
        # Compare the guess with the random number
        guessed_correctly = compare_guess(guess, random_number)
    
    # Print the number of guesses taken by the user
    print(f"You guessed the number in {number_of_guesses} attempts.")

# Main program loop
while True:
    # Play the game
    play_game()
    
    # Ask the user if they want to play again or exit
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    # Check if the user wants to exit
    if play_again == 'yes':
        continue
    elif play_again == 'no':
        break