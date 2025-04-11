
AFFIRMATION: str = "I am capable of doing anything I put my mind to." 

def main():
    print(f"Please write the following affirmation {AFFIRMATION}",end="")
    user_input: str = input("\033[34m")

    # The loop will iterate until the user_input is equal to the affirmation.
    while user_input != AFFIRMATION:
        
        print("\033[0m" , end = "")
        # Check if the user_input is not equal to the affirmation and print a message.
        # If the user_input is not equal to the affirmation, print "Hmmm That was not the affirmation"
        print("Hmmm That was not the affirmation")
        print("Please type the affirmation: " , end = "")
        user_input: str = input("\033[34m")
        print("\033[0m" , end = "")
    # If the user_input is equal to the affirmation, print "That's right!"
    print("\033[0mThat's right!")

if __name__ == "__main__":
    main()
        