def print_ones_digit(num: int):
    return num % 10

def main():
    num = int(input("\033[94mEnter a number: \033[0m"))
    ones_digit = print_ones_digit(num)
    print(f"Ones digit of {num} is {ones_digit}")

if __name__ == '__main__':
    main()