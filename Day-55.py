## 62.Text-based hangman code
import random

def choose_random_word():
    word_list = ["python", "java", "javascript", "ruby", "csharp", "html", "css"]
    return random.choice(word_list)

def play_hangman():
    word_to_guess = choose_random_word()
    guessed_letters = []
    attempts = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Try to guess the secret word. You have 6 attempts.")

    while attempts > 0:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"Word: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct guess!")
            if set(word_to_guess) == set(guessed_letters):
                print("Congratulations! You've guessed the word: " + word_to_guess)
                break
        else:
            print("Incorrect guess.")
            attempts -= 1

    if attempts == 0:
        print("You're out of attempts. The word was: " + word_to_guess)

if __name__ == "__main__":
    play_hangman()
