This repository hosts a small Python guessing game.

## Guess the Number Game
Run `python3 guess_the_number.py` to play a colorful number guessing game.
Use `--min` and `--max` to set the range and `--attempts` to limit guesses.
The `--cheat` option reveals the secret number for testing, and `--lang` lets you play in English or Greek.
Pass `--no-color` if you prefer plain text output.
Use `--seed` to reproduce games with a fixed random seed.
Run `--version` to see the current game version.
The banner width adapts automatically to fit the chosen language.

First, install the requirement:

```bash
pip install -r requirements.txt
```

```bash
python3 guess_the_number.py --min 1 --max 50 --attempts 5 --cheat --lang el --seed 42
```
At the end of your session, a colorized summary with your results will be displayed.

