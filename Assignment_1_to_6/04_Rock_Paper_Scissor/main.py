import random


def play():
    user: str = input("(r)Rock, (p)Paper or (s)Scissors? ").lower()

    computer: str = random.choice(["r", "p", "s"])

    print(f"You chose {user}, computer chose {computer}")

    if user == computer:
        return "It's a tie!"
    
    game = check_win(user, computer)
    if game:
        return "You win!"
    return "You lose!"

    
def check_win(user, computer):
    if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        return True
    return False


if __name__ == "__main__":
    print(play())