
INCHES_PER_FOOT: int = 12

def main():
    feet: float = float(input("Enter the number of feet: "))
    inches = feet * INCHES_PER_FOOT
    print(f"{feet} feet has {inches} inches!")

if __name__ == "__main__":
    main()
    