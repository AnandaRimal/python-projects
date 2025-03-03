import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = ["_"] * word_length
guessed_letters = set()

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single alphabetic character.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.add(guess)

    # Check guessed letter in the word
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print(f"Good guess! The word so far: {' '.join(display)}")
    else:
        print(f"You guessed '{guess}', which is not in the word. You lose a life.")
        lives -= 1

    # Check game-ending conditions
    if lives == 0:
        end_of_game = True
        print("You lose.")
        print(f"The word was: {chosen_word}")
    elif "_" not in display:
        end_of_game = True
        print("You win!")
        print(f"The word was: {''.join(display)}")

    # Display the current state of the hangman
    print(stages[lives])
