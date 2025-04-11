def main():
    """
    This program counts down from 10 to 0 and then prints "Liftoff!"
    """
    # The loop will iterate from 0 to 9 and print the countdown numbers.
    for i in range(10):
        # The loop will print the countdown numbers in reverse order.

        print(10-i, end=",")
        # The loop will pause for 1 second between each countdown number.
    print("Liftoff!")

if __name__ == "__main__":
    main()