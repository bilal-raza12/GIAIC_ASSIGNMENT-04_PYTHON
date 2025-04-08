def get_last_element(lst):
    
    if lst:
        return lst[-1]
    else:
        return None


def get_list():
    lst: list = []
    elem = input("Enter element to be added or press enter: ")
    while elem != "":
        lst.append(elem)
        elem = input(("Please enter elements to be added or press enter: "))

    return lst

def main():
    lst = get_list()
    last_elem = get_last_element(lst)
    if last_elem is not None:
        print(f"Last element in the list is: {last_elem}")
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()