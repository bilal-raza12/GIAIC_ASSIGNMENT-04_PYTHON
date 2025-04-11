def main():
  side1: float = float(input("What is the legnth of side1? "))
  side2: float = float(input("What is the legnth of side2? ")) 
  side3: float = float(input("What is the legnth of side3? "))
  perimeter: float = side1 + side2 + side3

  print(f"The perimeter of triangle is {perimeter}") 

if __name__ == "__main__":
  main()