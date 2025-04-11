import random


SIDES = 6
def roll_dice():
    dice1: int = random.randint(1,SIDES)
    dice2: int = random.randint(1,SIDES)
    total: int = dice1 + dice2
    print(f"The total is {total}")

def main():
    
    
    roll_dice()
    roll_dice()
    roll_dice() 
    

if __name__ == "__main__":
    main()