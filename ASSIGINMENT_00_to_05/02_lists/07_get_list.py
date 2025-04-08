


def get_list():
    lst: list = []
    elem = input("Enter element to be added or press enter: ")
    while elem != "":
        lst.append(elem)
        elem = input(("Please enter elements to be added or press enter: "))

    return lst

def main():
    lst = get_list()
    print("the list is: ", lst)

if __name__ == "__main__":
    main()