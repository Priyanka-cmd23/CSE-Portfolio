import random


def number_guessing_game():
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess the number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            return

    print(f"Game over! The number was {number}.")


if __name__ == "__main__":
    number_guessing_game()
