def main():
    numbers = [1,2,3,4,5]
    for i in range(len(numbers)):
        element = numbers[i]
        numbers[i] = element * 2
    print(numbers)
if __name__=="__main__":
    main()