def greetings(name):
    return f"Hello {name}!✌"

def main():
    name = input("\033[1;3mEnter your name: \033[0m")
    greeting_message = greetings(name)
    print(greeting_message)

if __name__ == '__main__':
    main()