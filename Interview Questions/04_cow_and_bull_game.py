import random

def generate_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:4])   # pick first 4 unique digits

def cows_and_bulls():
    secret = generate_number()
    attempts = 0

    print("Welcome to Cows and Bulls Game!")
    print("I have a 4-digit number with unique digits. Try to guess it!")

    while True:
        guess = input("\nEnter your 4-digit guess: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input! Enter exactly 4 digits.")
            continue

        attempts += 1
        cows = 0
        bulls = 0

        for i in range(4):
            if guess[i] == secret[i]:
                bulls += 1
            elif guess[i] in secret:
                cows += 1

        print(f"{bulls} Bulls, {cows} Cows")

        if bulls == 4:
            print(f"\n🎉 Congratulations! You guessed the number {secret} in {attempts} attempts.")
            break

cows_and_bulls()
