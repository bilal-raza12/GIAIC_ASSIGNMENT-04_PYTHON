ADULT_AGE = 18


def is_adult(age: int) -> bool:

    if age >= ADULT_AGE:
        return True
    else:
        return False
    
def main():
    age = int(input("\033[1mEnter your age: \033[0m"))
    print(is_adult(age))

if __name__ == '__main__':
    main()