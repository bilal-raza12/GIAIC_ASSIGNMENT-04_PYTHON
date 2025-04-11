
MIN_HEIGHT = 120
def main():
    # ger the height of the user
    while True:
        
        height: float = float(input("How tall are you? "))
        # Check if the user is tall enough to ride
        if height >= MIN_HEIGHT:
            print("You are tall enough to ride.")
        else:
            print("You are not tall enough to ride.")
        
if __name__ == "__main__":
    main()