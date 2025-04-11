C = 299792458

def energy():
    m: float = float(input("Enter the mass in kilogram(KG): "))

    e: float = m*C**2

    print("e = m * C^2...")
    print(f"m = {m}KG")
    print(f"C = {C}m/s")
    print(f"{e} Joules of energy!")

def main():
    energy()

if __name__ == "__main__":
    main()