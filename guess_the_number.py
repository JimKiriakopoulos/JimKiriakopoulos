import argparse
import random


def get_guess(prompt: str) -> int:
    """Prompt the user until they enter a valid integer."""
    while True:
        guess = input(prompt)
        try:
            return int(guess)
        except ValueError:
            print("Please enter a valid integer.")


def play_game(min_value: int, max_value: int, max_attempts: int | None) -> int | None:
    """Run the guessing game and return attempts or None if failed."""
    number = random.randint(min_value, max_value)
    print(f"I'm thinking of a number between {min_value} and {max_value}.")
    attempts = 0
    while True:
        guess_int = get_guess("Take a guess: ")
        attempts += 1
        if guess_int < number:
            print("Too low!")
        elif guess_int > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return attempts
        if max_attempts and attempts >= max_attempts:
            print(f"Out of attempts! The correct number was {number}.")
            return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Play a number guessing game.")
    parser.add_argument("--min", type=int, default=1, help="Minimum possible number.")
    parser.add_argument("--max", type=int, default=100, help="Maximum possible number.")
    parser.add_argument(
        "--attempts", type=int, default=0, help="Maximum attempts. 0 for unlimited."
    )
    args = parser.parse_args()

    max_attempts = args.attempts if args.attempts > 0 else None
    while True:
        play_game(args.min, args.max, max_attempts)
        again = input("Play again? (y/n) ").strip().lower()
        if not again.startswith("y"):
            break


if __name__ == "__main__":
    main()
