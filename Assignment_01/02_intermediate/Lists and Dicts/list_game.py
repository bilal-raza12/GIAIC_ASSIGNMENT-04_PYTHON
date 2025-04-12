def acess_element(lst , index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"
    
def modify_list(lst , index , value):
    try:
        lst[index] = value
        return lst
    except IndexError:
        return "Index out of range"
    
def slice_lst(lst , start , end):
    try:
        return lst[start:end]
    except IndexError:
        return "Index out of range"
    
def main():
    lst = ["Bilal" , "Ali" , "Ahmed" , "Sara" , "Aisha"]
    print(f"Current list: {lst}")
    choice: str = input("Choose an operation: acess, modify , slice (a/m/s): ").lower()
    
    if type(choice) != str:
        return "Invalid operation type"
    if choice == "a":
        index: int = int(input("Enter the index of the element you want to access: "))
        print(acess_element(lst , index))
    elif choice == "m":
        index: int = int(input("Enter the index of the element you want to modify: "))
        value: str = input("Enter the new value: ")
        print(modify_list(lst , index , value))
    elif choice == "s":
        start: int = int(input("Enter the start index for slicing: "))
        end: int = int(input("Enter the end index for slicing: "))
        print(slice_lst(lst , start , end))
    else:
        print("Invalid operation")


if __name__ == "__main__":
    main()