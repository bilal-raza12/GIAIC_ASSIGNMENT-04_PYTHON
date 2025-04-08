def get_numbers():
    num_list: list = []
    while True:
        num = input("\033[34mEnter a number: \033[0m")
        if num == "":
            break

        num = int(num)
        num_list.append(num)
    return num_list


def num_counts(num_list):
    
    num_dict: dict = {}
    for i in num_list:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(f"{str(num)} appears {str(num_dict[num])} times.")
def main():
    user_input = get_numbers()
    num_dict = num_counts(user_input)
    print_counts(num_dict)

if __name__ == "__main__":
    main()

