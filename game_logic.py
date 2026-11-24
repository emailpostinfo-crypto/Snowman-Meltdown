import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1
    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Guess only one letter!")
            continue
        print("You guessed:", guess)
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("The snowman was saved!")
            break
    if mistakes == max_mistakes:
        print(STAGES[mistakes])
        print("The snowman was not saved!")
        print(f"The searched word was: {secret_word}")


def play_again():
    print("\nThe game is over.\n")
    while True:
        answer = input(
            "Do you want to play again? Insert 'yes' or 'no': "
        ).lower().strip()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Invalid input. You must insert 'yes' or 'no'")
