# Mini Project: Number Guessing Game

import random

def number_guessing_game():
    print("=== Welcome to the Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!\n")

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.\n")

# Run the game
number_guessing_game()
