

Peturksbouipo = 16
Stanlau = 25
Mayengua = 48


def main():
    # Get the age of the user
    age = int(input("How old are you? "))

    # Check if the user is a child
    if age >= Peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is {Peturksbouipo}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {Peturksbouipo}.")

    if age >= Stanlau:
        print(f"You can vote in Stanlau where the voting age is {Stanlau}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {Stanlau}.")

    if age >= Mayengua:
        print(f"You can vote in Mayengua where the voting age is {Mayengua}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {Mayengua}.") 


if __name__ == "__main__":
    main()