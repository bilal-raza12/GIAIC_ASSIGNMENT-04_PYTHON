def main():
    user_input: int = int(input("Enter a number: "))
    result: int = user_input * 2
    while True:
        print(result , end=" ")
        result *= 2
        if result >= 100:
            print(result)
            break
        
if __name__ == "__main__":
    main() 
