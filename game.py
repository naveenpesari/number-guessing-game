"""
Number Guessing Game
Internship Project - Think Champ Pvt Ltd

A console-based number guessing game where the player tries to guess
a randomly generated secret number within a limited number of attempts.

Features:
- Random secret number generation within a chosen range
- Limited attempts based on difficulty level
- "Too High" / "Too Low" hints after every guess
- Win / Game Over messages
- Input validation (won't crash on bad input)
- Play again option
- Bonus: difficulty levels, leaderboard, and remaining-attempts countdown
"""

import random

# ---------------------------------------------------------------------------
# Difficulty configuration: name -> (lower bound, upper bound, max attempts)
# ---------------------------------------------------------------------------
DIFFICULTY_LEVELS = {
    "1": ("Easy", 1, 50, 10),
    "2": ("Medium", 1, 100, 7),
    "3": ("Hard", 1, 200, 6),
}

# Leaderboard is kept in memory for the current run of the program.
# Stores tuples of (difficulty_name, attempts_used)
leaderboard = []


def choose_difficulty():
    """Ask the player to pick a difficulty level. Returns (name, low, high, max_attempts)."""
    print("\nChoose a difficulty level:")
    print("  1. Easy   (1-50,  10 attempts)")
    print("  2. Medium (1-100, 7 attempts)")
    print("  3. Hard   (1-200, 6 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in DIFFICULTY_LEVELS:
            return DIFFICULTY_LEVELS[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


def get_valid_guess(low, high):
    """Keep asking until the player enters a valid integer within range.
    Handles non-numeric input gracefully without crashing the program."""
    while True:
        raw = input(f"Enter your guess ({low}-{high}): ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("That's not a valid whole number. Please try again.")
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def play_round():
    """Plays a single round of the game and returns True if the player wants to play again."""
    name, low, high, max_attempts = choose_difficulty()
    secret_number = random.randint(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    for attempt in range(1, max_attempts + 1):
        remaining = max_attempts - attempt + 1
        print(f"Attempt {attempt} of {max_attempts} (remaining: {remaining})")
        guess = get_valid_guess(low, high)

        if guess == secret_number:
            print(f"\nCorrect! You guessed it in {attempt} attempt(s).")
            leaderboard.append((name, attempt))
            break
        elif guess < secret_number:
            print("Too Low!\n")
        else:
            print("Too High!\n")
    else:
        # This 'else' runs only if the for-loop completes without 'break' (i.e. no correct guess)
        print(f"\nGame Over! You've used all {max_attempts} attempts.")
        print(f"The correct number was {secret_number}.")

    show_leaderboard()

    again = input("\nDo you want to play again? (y/n): ").strip().lower()
    return again in ("y", "yes")


def show_leaderboard():
    """Displays the best (fewest attempts) scores recorded so far in this session."""
    if not leaderboard:
        return
    print("\n--- Leaderboard (fewest attempts, this session) ---")
    top_scores = sorted(leaderboard, key=lambda entry: entry[1])[:5]
    for i, (difficulty, attempts) in enumerate(top_scores, start=1):
        print(f"{i}. {difficulty} - {attempts} attempt(s)")
    print("----------------------------------------------------")


def main():
    print("=" * 50)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 50)

    playing = True
    while playing:
        playing = play_round()

    print("\nThanks for playing! Goodbye.")


if __name__ == "__main__":
    main()
