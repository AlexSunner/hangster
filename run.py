import random

def choose_word():
    """ 
    Random words from a predefined list 
    """
    words = ["workspace", "develop", "programming", "python", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Display the current state of the word, 
    showing guessed letters and placeholders for unguessed letters
    """
    display = " "
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        return display

def hangman():
    """
    Main function to run the game.
    The function validates the user input,
    Checks if the letter has already been guessed,
    Add the guessed letter to the list,
    Checks if the guessed letter is not in the word,
    Checks if the players has more attempts, if not, game over.
    """
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()

    print("Welcome to Hangster!")

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Current word: {current_display}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            