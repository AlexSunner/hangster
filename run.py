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

def main():
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

    print("Welcome to Hangster! \n")
    print("---------------------------")
    print("Guess the correct word - You have 6 attempts! \n")

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Current word: {current_display}")
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
            print(f"Incorrect! Attempts left: {max_attempts}")

            if max_attempts == 0:
                print("Game over! The word was:", word_to_guess)
                break
        else:
            print("Correct guess!")

        if set(guessed_letters) >= set(word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    main()