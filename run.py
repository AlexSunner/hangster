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