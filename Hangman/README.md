Hangman Game

Description

The Hangman Game is a Python-based word-guessing game where players attempt to guess a hidden word one letter at a time. The player has a limited number of lives and loses a life for every incorrect guess. The game ends when the player successfully guesses the word or runs out of lives.

Features

Randomly selects a word from a predefined list.

Tracks guessed letters to avoid duplicate guesses.

Displays a visual representation of the hangman with each incorrect guess.

Ends the game when the word is fully guessed or the player runs out of lives.

How It Works

A random word is chosen at the start of the game.

The player inputs a letter guess.

If the letter is in the word, it is revealed in the correct position(s).

If the letter is not in the word, the player loses a life.

The game continues until the word is guessed or all lives are lost.

Example Output

Guess a letter: e
Good guess! The word so far: _ e _ _ _

Guess a letter: a
You guessed 'a', which is not in the word. You lose a life.

You lose.
The word was: apple

Installation & Usage

Ensure Python is installed (Python 3 recommended).

Save the script as hangman.py.

Create hangman_words.py containing a list of words.

Create hangman_art.py containing ASCII art for the hangman.

Run the script:

python hangman.py

Notes

The game is case-insensitive (treats uppercase and lowercase the same).

Only single-letter alphabetical inputs are accepted.

License

This project is open-source and free to use for fun purposes!


