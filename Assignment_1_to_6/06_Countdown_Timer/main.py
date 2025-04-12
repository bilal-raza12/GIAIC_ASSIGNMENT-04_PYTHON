import time 

# Countdown Timer
def countdown(t):
    # This function takes the time in seconds as input and counts down to zero.
    # It prints the time remaining in MM:SS format.
    # The countdown continues until the time reaches zero.
    # The function uses the time.sleep() method to create a delay of one second between each decrement.
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time's up!")  # Print a message when the countdown reaches zero


if __name__ == "__main__":

    t = int(input("Enter the time in seconds: "))  # Prompt the user to enter the countdown time in seconds
    countdown(t)  # Call the countdown function with the user-provided time
# This code implements a simple countdown timer in Python.