

def main():

    noun1 = input("Noun 1: ")
    noun2 = input("Noun 2: ")
    adj1 = input("Adjective 1: ")
    adj2 = input("Adjective 2: ")
    verb1 = input("Verb 1: ")
    verb2 = input("Verb 2: ")
    verb3 = input("Verb 3: ")

    # Madlib Story
    madlib = f"""Yesterday, I went to the {noun1} and saw a {adj1} {noun2} jumping up and down in its tree.
He {verb1} loudly and {verb2} with a group of kids.
Everyone was {verb3} and having a crazy time.
It was the most {adj2}  day ever!"""
    print(madlib)

if __name__ == "__main__":
    main()