def main():
    num1: int = int(input("Plaese enter an integer to be divided: "))
    num2: int = int(input("Please enter an integer to divided with: "))
    if num1 == 0 or num2 == 0:
        print("Invalid Number!! Must be greater than 0") 
    else:

        div: int = num1 // num2
        rem: int = num1 % num2
        print(f"The division is {div} and remainder is {rem}")

if __name__ == "__main__":
    main()

