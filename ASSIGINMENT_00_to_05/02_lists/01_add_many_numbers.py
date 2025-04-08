def add_numbers(numbers) -> int:
    sum = 0
    for i in numbers:
        sum += i
    
    return sum

def main():
    numbers: list = [1,2,3,4,5,6]
    sum: int = add_numbers(numbers)
    print(f"The Total sum is: {sum}")

if __name__ == "__main__":
    main()
