def divisor(x):
    for i in range(1,x+1):
        if x % i == 0:
            print(i , end=" ")  # Print the divisor followed by a space

def main():
    num = int(input("\033[94mEnter a number: \033[0m"))
    print(f"Divisors of {num} are:")
    divisor(num)

if __name__ == '__main__':
    main()