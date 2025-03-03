# Blackjack Project

## Introduction
This is a simple Python-based Blackjack game where the user plays against the computer. The game follows basic Blackjack rules, allowing the user to draw an extra card and determining the winner based on their total scores.

## How to Play
1. The program starts by dealing two random cards to both the user and the computer.
2. The scores of both hands are calculated.
3. If either player has a Blackjack (a total of 21 with the first two cards), the game ends immediately with a winner.
4. The user is asked if they want to add an additional card.
5. The computer will automatically draw an additional card if its score is below 17.
6. The winner is determined based on whose score is closest to 21 without exceeding it.

## Rules
- Aces (11) can make a hand bust, but in this implementation, it is always counted as 11.
- Face cards (J, Q, K) are valued at 10.
- If both players exceed 21, the game results in no winner.
- If one player exceeds 21 while the other does not, the player who did not exceed wins.
- If both players have the same total, it's a tie.

## Installation and Running the Game
1. Ensure you have Python installed.
2. Copy and save the script as `blackjack.py`.
3. Run the script using:
   ```sh
   python blackjack.py
   ```

## Future Improvements
- Implement Ace as 1 or 11 based on hand value.
- Allow multiple rounds with score tracking.
- Add a betting system.
- Improve computer AI to make smarter decisions.

Enjoy playing Blackjack!
