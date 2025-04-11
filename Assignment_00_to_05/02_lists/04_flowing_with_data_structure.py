def add_three_copies(my_list , data):

    for i in range(3):
         my_list.append(data)
    

def main():
     lst = []
     data = input("Enter the data to be added: ")
     add_three_copies(lst,data)
     print(f"List after 3 copies {lst}")
    
     

if __name__ == "__main__":
    main()