import random


def guess_number(x):
    guess_number: int = random.randint(1, x)

    guess: int = 0

    while guess != guess_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < guess_number:
            print("Sorry, too low.")
        elif guess > guess_number:
            print("Sorry, too high.")

        else: 
            print(f"Yay! You guessed the number {guess_number} correctly!")

if __name__ == "__main__":
    guess_number(10)