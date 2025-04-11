# importing the hashlib library to hash passwords
import hashlib


# This program demonstrates a simple login system using hashed passwords.
def hash_password(password):
    """
    Hashes a password using SHA-256 algorithm.


    """
    return hashlib.sha256(password.encode()).hexdigest()


# The login function checks if the email exists in the stored login dictionary and verifies the password.
def login(email , password_to_check , stored_login):
    """
    Checks if the email exists in the stored login dictionary and verifies the password.
    """
    if email in stored_login:
        if stored_login[email] == hash_password(password_to_check):
            return True
        else:
            return False
        

# The main function initializes a dictionary with stored logins and prompts the user for their email and password.
def main():
    """
    Initializes a dictionary with stored logins and prompts the user for their email and password.
    """
    stored_login = {
        "example123@gmail.com": hash_password("password123"),
        "example234@hotmail.com": hash_password("password234"),
    }

    # Prompting the user for their email and password

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Checking if the login is successful
    if login(email, password, stored_login):
        print("Login Successful")
    else:
        print("Login Failed")


if __name__ == "__main__":
    main()
