def get_user_data():
    fname: str = input("What is yuor first name? ")
    lname: str = input("What is your last name? ")
    email: str = input("What is your email? ")

    return fname, lname, email


def main():
    print(f"Recived following information: {get_user_data()}")

if __name__ == '__main__':
    main()