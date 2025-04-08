MAX_LENGTH: int = 5
def shorten(lst):
    """
    Shorten the list to a maximum length of MAX_LENGTH.
    If the list is longer than MAX_LENGTH, it will be truncated.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"Removed item: {last_elem}")
    
  
    

def get_list():

    lst: list = []
    elem = input("Enter element to be added or press enter: ")
    while elem != "":
        lst.append(elem)
        elem = input(("Please enter elements to be added or press enter: "))

    return lst

def main():
     lst = get_list()
     
     shorten(lst)

if __name__ == "__main__":
     main()