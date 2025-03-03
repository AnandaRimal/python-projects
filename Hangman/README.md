# Hangman Game

## Description
The Hangman game is a word-guessing game where the player tries to guess a hidden word one letter at a time before running out of lives. The game features visual hangman stages and interactive gameplay.

## Features
- Randomly selects a word from a predefined list
- Allows the player to guess letters
- Tracks guessed letters and prevents duplicate guesses
- Displays the hangman stages as lives decrease
- Provides feedback on correct and incorrect guesses

## How It Works
1. The program selects a random word from `hangman_words.py`.
2. The player guesses one letter at a time.
3. Correct guesses reveal the letters in the word.
4. Incorrect guesses decrease the number of lives and update the hangman graphic.
5. The player wins by guessing all letters correctly before running out of lives.
6. The player loses if all lives are depleted before guessing the word.

## Example Output
```
Welcome to Hangman!
Guess a letter: a
Good guess! The word so far: _ a _ _ _

Guess a letter: x
You guessed 'x', which is not in the word. You lose a life.

You win!
The word was: apple
```

## Installation & Usage
1. Ensure you have Python installed (Python 3 recommended).
2. Save the script as `hangman.py` and include `hangman_words.py` and `hangman_art.py`.
3. Run the script:
   ```sh
   python hangman.py
   ```

## Notes
- The game uses predefined words from `hangman_words.py`.
- Hangman graphics are stored in `hangman_art.py`.

## License
This project is open-source and free to use for fun purposes!

