#!/usr/bin/env python3
"""Simple command-line number guessing game with optional colors.

Use ``--seed`` for reproducible results when testing. The ``--games`` option
plays multiple rounds automatically. ``--banner`` lets you customize the title
shown at start.
"""

import argparse
import random
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class GameResult:
    """Outcome of a single game round."""

    won: bool
    attempts: int


__version__ = "1.2.0"

try:
    from colorama import Fore, init

    COLORAMA_AVAILABLE = True
except ModuleNotFoundError:  # pragma: no cover - graceful fallback
    COLORAMA_AVAILABLE = False

    class Fore:
        """Fallback color constants when ``colorama`` isn't installed."""

        RED = GREEN = CYAN = MAGENTA = ""

    def init(*_args: object, **_kwargs: object) -> None:
        """Dummy init when colorama is not available."""
        return None


init(autoreset=True)


MESSAGES: Dict[str, Dict[str, str]] = {
    "en": {
        "banner": "GUESS THE NUMBER",
        "thinking": "I'm thinking of a number between {min} and {max}.",
        "cheat": "(Cheat) Secret number is {number}",
        "prompt": "Take a guess: ",
        "out_of_range": "Guess a number between {min} and {max}.",
        "invalid": "Please enter a valid integer.",
        "too_low": "Too low!",
        "too_high": "Too high!",
        "congrats": "Congratulations! You guessed the number in {attempts} attempts.",
        "out_of_attempts": "Out of attempts! The correct number was {number}.",
        "attempts_remaining": "{remaining} attempts remaining.",
        "play_again": "Play again? (y/n) ",
        "summary": "\nGame summary:",
        "game_lost": "Game {i}: lost",
        "game_won": "Game {i}: won in {attempts} attempts",
        "won_stats": "You won {wins} out of {total} games!",
        "avg_attempts": "Average attempts on wins: {avg:.1f}",
        "no_wins": "No wins this time.",
        "thanks": "Thanks for playing!",
        "interrupted": "\nInterrupted.",
    },
    "el": {
        "banner": "ΜΑΝΤΕΨΕ ΤΟΝ ΑΡΙΘΜΟ",
        "thinking": "Σκέφτομαι έναν αριθμό ανάμεσα στο {min} και {max}.",
        "cheat": "(Cheat) Το μυστικό νούμερο είναι {number}",
        "prompt": "Μάντεψε: ",
        "out_of_range": "Μάντεψε αριθμό ανάμεσα στο {min} και {max}.",
        "invalid": "Παρακαλώ γράψε έναν έγκυρο ακέραιο.",
        "too_low": "Πολύ μικρός!",
        "too_high": "Πολύ μεγάλος!",
        "congrats": "Μπράβο! Το βρήκες σε {attempts} προσπάθειες.",
        "out_of_attempts": "Τέλος προσπαθειών! Ο σωστός αριθμός ήταν {number}.",
        "attempts_remaining": "Απομένουν {remaining} προσπάθειες.",
        "play_again": "Θες να παίξεις ξανά; (y/n) ",
        "summary": "\nΠερίληψη παιχνιδιού:",
        "game_lost": "Παιχνίδι {i}: έχασες",
        "game_won": "Παιχνίδι {i}: νίκη σε {attempts} προσπάθειες",
        "won_stats": "Κέρδισες {wins} από τα {total} παιχνίδια!",
        "avg_attempts": "Μέσος όρος προσπαθειών στις νίκες: {avg:.1f}",
        "no_wins": "Καμία νίκη αυτή τη φορά.",
        "thanks": "Ευχαριστούμε για το παιχνίδι!",
        "interrupted": "\nΔιακόπηκε.",
    },
}


def get_guess(prompt: str, error_msg: str) -> int:
    """Prompt the user until they enter a valid integer."""
    while True:
        guess = input(prompt)
        try:
            return int(guess)
        except ValueError:
            print(error_msg)


def print_banner(text: str, min_width: int = 30) -> None:
    """Display a simple banner for the game."""
    width = max(min_width, len(text) + 4)
    top = "╔" + "═" * width + "╗"
    middle = "║" + text.center(width) + "║"
    bottom = "╚" + "═" * width + "╝"
    banner_text = "\n" + "\n".join([top, middle, bottom])
    print(Fore.CYAN + banner_text)


def play_game(
    min_value: int,
    max_value: int,
    max_attempts: Optional[int],
    cheat: bool,
    messages: Dict[str, str],
) -> GameResult:
    """Run one round and report whether the player won and how many attempts."""
    number = random.randint(min_value, max_value)
    print(messages["thinking"].format(min=min_value, max=max_value))
    if cheat:
        print(Fore.MAGENTA + messages["cheat"].format(number=number))
    attempts = 0
    while True:
        guess_int = get_guess(messages["prompt"], messages["invalid"])
        if not min_value <= guess_int <= max_value:
            print(
                Fore.RED + messages["out_of_range"].format(min=min_value, max=max_value)
            )
            continue
        attempts += 1
        if guess_int < number:
            print(Fore.RED + messages["too_low"])
        elif guess_int > number:
            print(Fore.RED + messages["too_high"])
        else:
            print(Fore.GREEN + messages["congrats"].format(attempts=attempts))
            return GameResult(True, attempts)
        if max_attempts:
            remaining = max_attempts - attempts
            if remaining <= 0:
                print(Fore.RED + messages["out_of_attempts"].format(number=number))
                return GameResult(False, attempts)
            print(messages["attempts_remaining"].format(remaining=remaining))


def main() -> None:
    """Parse arguments and launch the guessing game."""
    parser = argparse.ArgumentParser(description="Play a number guessing game.")
    parser.add_argument("--min", type=int, default=1, help="Minimum possible number.")
    parser.add_argument("--max", type=int, default=100, help="Maximum possible number.")
    parser.add_argument(
        "--attempts",
        type=int,
        default=0,
        help="Maximum attempts. 0 for unlimited.",
    )
    parser.add_argument(
        "--cheat",
        action="store_true",
        help="Display the secret number at the start for debugging.",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output even if colorama is installed.",
    )
    parser.add_argument(
        "--lang",
        choices=sorted(MESSAGES.keys()),
        default="en",
        help="Language for messages (en or el).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Optional random seed for reproducible sessions.",
    )
    parser.add_argument(
        "--banner",
        type=str,
        help="Custom banner text shown at startup.",
    )
    parser.add_argument(
        "--games",
        type=int,
        default=0,
        help="Automatically play this many games in a row.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Show program's version number and exit.",
    )
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.attempts < 0:
        parser.error("--attempts must be non-negative")

    if args.games < 0:
        parser.error("--games must be non-negative")

    if args.min >= args.max:
        parser.error("--min must be less than --max")

    if args.no_color or not COLORAMA_AVAILABLE:
        for attr in ("RED", "GREEN", "CYAN", "MAGENTA"):
            setattr(Fore, attr, "")

    messages = MESSAGES[args.lang]
    banner_text = args.banner if args.banner else messages["banner"]
    print_banner(banner_text)
    max_attempts = args.attempts if args.attempts > 0 else None
    results: List[GameResult] = []
    played = 0
    try:
        while True:
            result = play_game(args.min, args.max, max_attempts, args.cheat, messages)
            results.append(result)
            played += 1
            if args.games:
                if played >= args.games:
                    break
            else:
                again = input(messages["play_again"]).strip().lower()
                if not again.startswith("y"):
                    break
    except (KeyboardInterrupt, EOFError):
        print(messages["interrupted"])

    if results:
        print(messages["summary"])
        for i, r in enumerate(results, 1):
            if not r.won:
                print(messages["game_lost"].format(i=i))
            else:
                print(messages["game_won"].format(i=i, attempts=r.attempts))
        wins = sum(1 for r in results if r.won)
        if wins:
            avg = sum(r.attempts for r in results if r.won) / wins
            print(
                Fore.GREEN + messages["won_stats"].format(wins=wins, total=len(results))
            )
            print(messages["avg_attempts"].format(avg=avg))
        else:
            print(Fore.RED + messages["no_wins"])
    print(messages["thanks"])


if __name__ == "__main__":
    main()
