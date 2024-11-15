import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts to guess the correct number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Run the game
guessing_game()
