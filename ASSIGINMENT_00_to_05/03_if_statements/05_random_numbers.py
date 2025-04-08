import random


def main():
    # Generate random numbers
    for i in range(10):
        random_number = random.randint(1, 100)
        print(random_number)
    
if __name__ == "__main__":
    main()