import random

def hangman():
    # List of words to guess
    words = ["python", "hangman", "programming", "developer", "computer", "science"]
    word = random.choice(words)  # choose a random word
    guessed = "_" * len(word)    # start with blanks
    guessed = list(guessed)      # make it mutable
    attempts = 10
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, ch in enumerate(word):
                if ch == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word. Attempts left: {attempts}")

        print(" ".join(guessed))

    if "_" not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Out of attempts! The word was:", word)

hangman()
