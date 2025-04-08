def phone_book_entry():

    # Initialize an empty dictionary to store the phonebook entries
    phonebook = {}



     # Prompt the user to enter names and numbers until an empty name is entered
    while True:
        # Prompt the user for a name and number
        name = input("Enter a name (or press enter): ")
        if name == "":
            break
        number = input("Enter a number: ")
        phonebook[name] = number
    # Print the phonebook entries
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")
    return phonebook
    

def search_number(phonebook):
    
    # Prompt the user for a name to search for
    while True:

        name = input("Enter a name to search for: ")
        if name == "":
            break
    
    # Check if the name exists in the phonebook
        if name not in phonebook:
            print(f"{name} not found in phonebook")
        else:
            print(phonebook[name])

def main():
    # Create a phonebook entry
    phonebook = phone_book_entry()
    # Search for a number in the phonebook
    search_number(phonebook)

if __name__ == "__main__":
    main()
