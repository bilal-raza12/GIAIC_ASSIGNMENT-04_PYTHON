def print_multiple(message, times):
    for _ in range(times):
        print(message , end=" ")  

def main():
    message = input("\033[94mEnter a message: \033[0m")
    times = int(input("\033[94mHow many times to print? \033[0m"))
    print_multiple(message, times)

if __name__ == '__main__':
    main()