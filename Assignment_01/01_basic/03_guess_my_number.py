import random
def main():
    print("I am thinking of a number between 1 and 99." , end=" ")
    user_input: int = int(input("Enter a guess: "))
    random_number: int = random.randint(1, 100)

    while True:
        if user_input < random_number:
            print("Yur guess is too low")
            #
        elif user_input > random_number:
            print("Your guess is too high.")
            
        else:
            print(f"Congrat's! The number was {random_number}.")
            break
        user_input = int(input("Enter a new number: "))

if __name__ == "__main__":
    main()