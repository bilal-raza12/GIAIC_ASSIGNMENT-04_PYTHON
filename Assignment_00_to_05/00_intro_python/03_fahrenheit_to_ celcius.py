def main():
  Fahrenheit: float = float(input("Enter the temperature in Fehrenhiet: "))

  celcius: float = (Fahrenheit - 32) * 5.0/9.0

  print(f"{Fahrenheit} degrees Fahrenheit is %.2f "  % (celcius)  , "degrees Celcius")

if __name__ == "__main__":
  main()