# Guess the Number Game

This repository contains a small Python guessing game. To play, run:

```bash
python3 guess_the_number.py
```

Use the command-line options to customize gameplay:

- `--min` and `--max` define the range of numbers
- `--attempts` limits guesses (0 for unlimited)
- `--cheat` reveals the secret number
- `--lang` chooses the message language (`en` or `el`)
- `--no-color` disables colored output
- `--banner` customizes the startup banner text
- `--games` runs multiple rounds without prompting
- `--seed` sets the random seed for reproducible sessions
- `--version` shows the program version

Install dependencies with:

```bash
pip install -r requirements.txt
```

Run the automated tests with:

```bash
python3 -m unittest -v
```
