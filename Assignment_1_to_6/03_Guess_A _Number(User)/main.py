import random


def computer_guess(x):
    low: int = 1
    high: int = x
    feedback: str = ""
    attempts: int = 5

    while feedback != "c":
        if low != high:
            guess: int = random.randint(low, high)
        else:
            guess: int = low  # or high, since they are the same

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        attempts += 1
        if attempts <= 0:
            print("Better luck next time...")

    print(f"Yay! The computer guessed your number {guess} correctly!")


if __name__ == "__main__":
    computer_guess(10)