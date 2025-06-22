
import random

def guessing_game(low=1, high=100, max_attempts=None):
    """
    Classic number-guessing game.
    The computer picks a random number between `low` and `high`.
    The player keeps guessing until correct or attempts run out.
    """
    secret = random.randint(low, high)
    print(f"I'm thinking of a number between {low} and {high}.")

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
            break

        if max_attempts is not None and attempts >= max_attempts:
            print(f"Out of tries! The number was {secret}.")
            break


if __name__ == "__main__":
    # play with a 1-90 range and an optional 7-try limit
    guessing_game(1, 90, max_attempts=7)
