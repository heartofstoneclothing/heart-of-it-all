import random

def guess_the_number():
    print("Welcome to Guess the Number!")

    while True:
        # Generate a random number between 1 and 100 for each new game
        secret_number = random.randint(1, 100)
        attempts = 0

        while True:
            # Get the player's guess
            guess = input("Enter your guess (1-100), 'r' to reset, or 'q' to quit: ")

            if guess.lower() == 'q':
                print("Exiting the game. Goodbye!")
                return
            elif guess.lower() == 'r':
                print("Resetting the game...")
                break

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number, 'r' to reset, or 'q' to quit.")
                continue

            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

if __name__ == "__main__":
    guess_the_number()
