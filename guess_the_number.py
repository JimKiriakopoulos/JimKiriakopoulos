"""Simple command-line number guessing game with optional colors."""

import argparse
import random
from typing import List, Optional

try:
    from colorama import Fore, init
except ModuleNotFoundError:  # pragma: no cover - graceful fallback
    class Fore:
        RED = GREEN = CYAN = MAGENTA = ""

    def init(*_args: object, **_kwargs: object) -> None:
        """Dummy init when colorama is not available."""
        pass

init(autoreset=True)


def get_guess(prompt: str) -> int:
    """Prompt the user until they enter a valid integer."""
    while True:
        guess = input(prompt)
        try:
            return int(guess)
        except ValueError:
            print("Please enter a valid integer.")


def print_banner() -> None:
    """Display a simple banner for the game."""
    banner = (
        "\n"
        "╔══════════════════════════════╗\n"
        "║        GUESS THE NUMBER       ║\n"
        "╚══════════════════════════════╝"
    )
    banner_text = "".join(banner)
    print(Fore.CYAN + banner_text)


def play_game(
    min_value: int, max_value: int, max_attempts: Optional[int], cheat: bool = False
) -> Optional[int]:
    """Run the guessing game and return attempts or None if failed."""
    number = random.randint(min_value, max_value)
    print(f"I'm thinking of a number between {min_value} and {max_value}.")
    if cheat:
        print(Fore.MAGENTA + f"(Cheat) Secret number is {number}")
    attempts = 0
    while True:
        guess_int = get_guess("Take a guess: ")
        attempts += 1
        if guess_int < number:
            print(Fore.RED + "Too low!")
        elif guess_int > number:
            print(Fore.RED + "Too high!")
        else:
            print(Fore.GREEN + f"Congratulations! You guessed the number in {attempts} attempts.")
            return attempts
        if max_attempts:
            remaining = max_attempts - attempts
            if remaining <= 0:
                print(Fore.RED + f"Out of attempts! The correct number was {number}.")
                return None
            else:
                print(f"{remaining} attempts remaining.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Play a number guessing game.")
    parser.add_argument("--min", type=int, default=1, help="Minimum possible number.")
    parser.add_argument("--max", type=int, default=100, help="Maximum possible number.")
    parser.add_argument(
        "--attempts", type=int, default=0, help="Maximum attempts. 0 for unlimited."
    )
    parser.add_argument(
        "--cheat",
        action="store_true",
        help="Display the secret number at the start for debugging.",
    )
    args = parser.parse_args()

    if args.min >= args.max:
        parser.error("--min must be less than --max")

    print_banner()
    max_attempts = args.attempts if args.attempts > 0 else None
    results: List[Optional[int]] = []
    try:
        while True:
            result = play_game(args.min, args.max, max_attempts, args.cheat)
            results.append(result)
            again = input("Play again? (y/n) ").strip().lower()
            if not again.startswith("y"):
                break
    except KeyboardInterrupt:
        print("\nInterrupted.")

    if results:
        print("\nGame summary:")
        for i, r in enumerate(results, 1):
            if r is None:
                print(f"Game {i}: lost")
            else:
                print(f"Game {i}: won in {r} attempts")
        wins = sum(1 for r in results if r is not None)
        if wins:
            avg = sum(r for r in results if r is not None) / wins
            print(Fore.GREEN + f"You won {wins} out of {len(results)} games!")
            print(f"Average attempts on wins: {avg:.1f}")
        else:
            print(Fore.RED + "No wins this time.")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
