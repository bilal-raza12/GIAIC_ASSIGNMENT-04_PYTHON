import random
import string
def genrate_password(length , passwords_count):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []
    for _ in range(passwords_count):
        password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)
    return passwords

def main():
    length = int(input("Enter the length of the password: "))
    passwords_count = int(input("Enter the number of passwords to generate: "))
    passwords = genrate_password(length, passwords_count)
    print("Generated Passwords:")
    for password in passwords:
        print(password)


if __name__ == "__main__":
    main()