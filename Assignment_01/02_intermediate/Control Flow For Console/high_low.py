import random

def main():
    NUM_ROUNDS: int = 5
    rounds: int = 1
    score: int = 0
    print("Welcome To The High Low Game!")
    print("------------------------------")

    user_number: int = random.randint(1, 100)
    comp_number: int = random.randint(1, 100)
    
    while True:
        print(f"Round {rounds}") 
        print(f"Your number is {user_number}.")
        user_input = input("Do you think yur number is higher or lower than the computer's? ")
        if user_input.lower() == "higher":
            if user_number > comp_number or user_number == comp_number:
                print("You are right")
                score += 1
            else:
                print(f"Aww that's incorect. The computer's number was {comp_number}.")
            
        else:
            if user_number < comp_number or user_number == comp_number:
                print("You are right")
                score += 1
            else:
                    print(f"Aww that's incorect. The computer's number was {comp_number}.")
        
        print(f"Your score is now {score}.")
        print("\n")
        rounds += 1
        if NUM_ROUNDS == 0:
            print("\n\n\nBetter luck next time")
            break
        NUM_ROUNDS -= 1

if __name__ == "__main__":
    main()
            
    