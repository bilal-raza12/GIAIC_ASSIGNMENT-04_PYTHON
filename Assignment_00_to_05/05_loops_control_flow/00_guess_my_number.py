# import random module to generate a random number
import random

def main():
    """
    This programme will generate a random number between 1 and 99 and ask the user to guess it.
    
    
    """
    guess_number = random.randint(1, 100)

    print("I am thinking of a number between 1 and 99 ....")

    # Prompting the user to guess the number
    user_input = int(input("Enter a number: "))
    # Loop until the user guesses the correct number
    # The loop will continue until the user_input is equal to the guess_number
    while user_input != guess_number:
        # Check if the guessed number is less than or greater than the generated number
        # If the guessed number is less than the generated number, print "Too low! Try again."
        # If the guessed number is greater than the generated number, print "Too high! Try again."
        if user_input < guess_number:
            print("too low! Try again.")
        elif user_input > guess_number:
            print("too high! Try again.")
            
        
        user_input = int(input("Enter a new number: "))
    print("Congratulations! you guessed a rght number")

if __name__ == "__main__":
    main()