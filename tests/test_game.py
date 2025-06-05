import subprocess
import unittest
from pathlib import Path


class GuessGameTest(unittest.TestCase):
    """Basic integration test for the guessing game."""

    def test_two_games_no_prompt(self):
        script = Path(__file__).resolve().parents[1] / "guess_the_number.py"
        result = subprocess.run(
            [
                "python3",
                str(script),
                "--min",
                "1",
                "--max",
                "2",
                "--attempts",
                "1",
                "--games",
                "2",
                "--seed",
                "1",
                "--no-color",
            ],
            input="1\n1\n",
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Game 2", result.stdout)

    def test_cheat_option_reveals_number(self):
        """Ensure --cheat displays the secret number."""
        script = Path(__file__).resolve().parents[1] / "guess_the_number.py"
        result = subprocess.run(
            [
                "python3",
                str(script),
                "--min",
                "1",
                "--max",
                "2",
                "--attempts",
                "1",
                "--cheat",
                "--no-color",
                "--games",
                "1",
                "--seed",
                "1",
                "--lang",
                "en",
            ],
            input="1\n",
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Secret number is", result.stdout)


if __name__ == "__main__":
    unittest.main()
