



def get_first_element(lst):
    
    if lst:
        return lst[0]
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
    first_elem = get_first_element(lst)
    if first_elem is not None:
        print(f"First element in the list is: {first_elem}")
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()