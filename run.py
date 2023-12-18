import random

def choose_word(difficulty):
    """ 
    Random words from a predefined list based on difficulty.
    """
    if difficulty == "easy":
        words = ["snow", "apple", "green", "play", "hat"]
    elif difficulty == "medium":
        words = ["christmas", "reindeer", "winter", "snowball", "presents"]
    elif difficulty == "hard":
        words = ["encapsulation", "inheritance", "polymorphism", "abstraction", "framework"]
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

def main():
    """
    Main function to run the game.
    Player gets to choose a difficulty level,
    The function validates the user input,
    Checks if the letter has already been guessed,
    Add the guessed letter to the list,
    Checks if the guessed letter is not in the word,
    Checks if the player has more attempts, if not, game over.
    """
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty level. Exiting.")
        return
    max_attempts = 6 if difficulty == "easy" else 5 if difficulty == "medium" else 4
    guessed_letters = []
    word_to_guess = choose_word(difficulty)

    print("---------------------------")
    print(f"Welcome to Hangster! Difficulty: {difficulty.capitalize()}")
    print("---------------------------")
    print(f"Guess the correct word - You have {max_attempts} attempts!")
    print("--------------------------- \n")

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