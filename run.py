import random


def print_colored_text(text, color):
    """Print colored text using ANSI escape codes."""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }

    if color not in colors:
        print(f"Invalid color '{color}'. Using default color.")
        color = 'white'

    print(f"{colors[color]}{text}{colors['reset']}")


def choose_word(difficulty):
    """
    Random words from a predefined list based on difficulty.
    """
    if difficulty == "easy":
        words = ["snow", "apple", "green", "play", "hat"]
    elif difficulty == "medium":
        words = ["christmas", "reindeer", "winter", "snowball", "presents"]
    elif difficulty == "hard":
        words = [
            "encapsulation",
            "inheritance",
            "polymorphism",
            "abstraction",
            "framework"
        ]
    else:
        raise ValueError("Invalid difficulty level.")

    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Display the current state of the word,
    showing guessed letters and placeholders for unguessed letters.
    """
    display = " "
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def print_hangman_art(incorrect_attempts):
    """Print ASCII art for Hangman based on incorrect attempts."""
    hangman_art = [
        """
         ------
         |    |
         |
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        """
    ]
    print(hangman_art[incorrect_attempts])


def main():
    """
    Main function to run the game.
    Player gets to choose a difficulty level,
    The function validates the user input,
    Checks if the letter has already been guessed,
    Add the guessed letter to the list,
    Displays guessed letters,
    Checks if the guessed letter is not in the word,
    Prints a hanging man depending on incorrect attempts,
    Checks if the player has more attempts, if not, game over.
    """
    while True:
        difficulty = input(
            "Choose a difficulty (easy, medium, hard): "
        ).lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        else:
            print_colored_text(
                "Invalid input. Please choose 'easy', 'medium', or 'hard'.",
                'red'
            )

    max_attempts = (
        6 if difficulty == "easy" else (
          5 if difficulty == "medium" else 4
        )
    )
    guessed_letters = []
    word_to_guess = choose_word(difficulty)

    print_colored_text("---------------------------", 'blue')
    print_colored_text(
        f"Welcome to Hangster! Difficulty: {difficulty.capitalize()}",
        'yellow'
    )
    print_colored_text("---------------------------", 'blue')
    print_colored_text(
        f"Guess the correct word - You have {max_attempts} attempts!",
        'yellow'
    )
    print_colored_text("--------------------------- \n", 'blue')

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Current word: {current_display}")

        if guessed_letters:
            print("Guessed letters:", ' '.join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            max_attempts -= 1
            print_hangman_art(6 - max_attempts)
            print_colored_text(
                f"Incorrect! Attempts left: {max_attempts}",
                'red'
            )

            if max_attempts == 0:
                print_colored_text(
                    "Game over! The word was: " + word_to_guess,
                    'red'
                )
                break
        else:
            print_colored_text("Correct guess!", 'green')

        if set(guessed_letters) >= set(word_to_guess):
            print_colored_text(
                "Congratulations! You guessed the word: " + word_to_guess,
                'green'
            )
            break


if __name__ == "__main__":
    main()
