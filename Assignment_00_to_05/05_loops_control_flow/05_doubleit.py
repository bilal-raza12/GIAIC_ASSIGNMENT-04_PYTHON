

def main():
    """
    This program doubles a user input number until the result exceeds 100.
    """
    # Prompting the user to enter a number
    user_input: int = int(input("Please enter a number: "))
    result: int = user_input * 2
    # The loop will continue until the result exceeds 100.
    while True:
        print(result , end=" ")
        result *= 2
        if result > 100:
            print(result)
            break

if __name__ == "__main__":
    main()

