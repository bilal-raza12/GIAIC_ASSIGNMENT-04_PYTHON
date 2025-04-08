def main():
    fruits_cost = {
        "banana": 12.5,
        "apple": 11,
        "orange": 24.5,
        "grape": 23.6,
        "kiwi": 30
    }

    total_cost = 0
    for fruit in fruits_cost:
        price = fruits_cost[fruit]
        quantity : int = int(input(f"\033[1mHow many ({fruit}) do you want? \033[0m"))
        total_cost += price * quantity
    
    print(f"The total cost is ${total_cost}")

if __name__ == "__main__":
    main()
