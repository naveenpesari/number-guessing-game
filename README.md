# Number Guessing Game

A simple console-based Number Guessing Game built for the Think Champ Pvt Ltd
internship assignment.

The program randomly picks a secret number and the player has to guess it
within a limited number of attempts, receiving "Too High" / "Too Low" hints
after every guess.

## Features

- Random secret number generation within a chosen range
- Limited number of attempts (varies by difficulty)
- "Too High" / "Too Low" hint after every guess
- Win message showing number of attempts used
- "Game Over" message revealing the number if all attempts are used
- Input validation — the program does not crash on non-numeric input
- Option to play again after each round

### Bonus features implemented

- **Difficulty levels**: Easy (1-50, 10 attempts), Medium (1-100, 7 attempts),
  Hard (1-200, 6 attempts)
- **Leaderboard**: tracks the best (fewest-attempt) scores for the current
  session and displays the top 5 after each round
- **Remaining attempts countdown**: shows how many attempts are left before
  every guess

## Requirements

- Python 3.7 or higher (no external libraries needed — uses only the
  built-in `random` module)

## How to Run

1. Make sure Python 3 is installed:
   ```bash
   python3 --version
   ```
2. Clone this repository (or download `game.py`):
   ```bash
   git clone https://github.com/<your-username>/number-guessing-game.git
   cd number-guessing-game
   ```
3. Run the game:
   ```bash
   python3 game.py
   ```
   On Windows, you can instead use:
   ```bash
   python game.py
   ```

## Sample Gameplay

```
==================================================
   Welcome to the Number Guessing Game!
==================================================

Choose a difficulty level:
  1. Easy   (1-50,  10 attempts)
  2. Medium (1-100, 7 attempts)
  3. Hard   (1-200, 6 attempts)
Enter choice (1/2/3): 2

I'm thinking of a number between 1 and 100.
You have 7 attempts. Good luck!

Attempt 1 of 7 (remaining: 7)
Enter your guess (1-100): 50
Too High!

Attempt 2 of 7 (remaining: 6)
Enter your guess (1-100): 25
Too Low!

Attempt 3 of 7 (remaining: 5)
Enter your guess (1-100): 37

Correct! You guessed it in 3 attempt(s).

--- Leaderboard (fewest attempts, this session) ---
1. Medium - 3 attempt(s)
----------------------------------------------------

Do you want to play again? (y/n): n

Thanks for playing! Goodbye.
```

## Project Structure

```
number-guessing-game/
├── game.py       # Main game source code
└── README.md     # Project documentation
```

## Author

Submitted as part of the Think Champ Pvt Ltd internship program.



naveen change 