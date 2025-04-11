
# this is a simple joke bot
# it will ask the user what they want?
# if they say joke, it will tell them a joke

PROMPT = input("\033[34mWhat do yo want?")
JOKE = " Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry , I only understamd jokes"

def main():
    if PROMPT.lower() == "joke":
        print(JOKE)
    else:
        print(SORRY)


if __name__ == "__main__":
    main()