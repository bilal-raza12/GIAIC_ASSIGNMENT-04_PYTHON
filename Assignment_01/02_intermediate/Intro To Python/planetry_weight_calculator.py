# Mercury: 37.6%
MERCURY: float = 37.6
# Venus: 88.9%
VENUS: float = 88.9

# Mars: 37.8%
MARS: float = 37.8
# Jupiter: 236.0%
JUPITER: int = 236.0
# Saturn: 108.1%
SATURN: float = 108.1
# Uranus: 81.5%
URANUS: float = 81.5
# Neptune: 114.0%
NEPTUNE: float = 114.0


def main():
    earth_weight: float = float(input("Enter your weight on Earth: "))
    planet: str = input("Enter a planet: ")

    planet = planet.title()

    planet_cal: float = 0
    if planet.upper() == "MERCURY":
        planet_cal = (MERCURY/100) * earth_weight
        
    elif planet.upper() == "VENUS":
        planet_cal = (VENUS/100) * earth_weight
    elif planet.upper() == "MARS":
        planet_cal = (MARS/100) * earth_weight
    elif planet.upper() == "JUPITER":
        planet_cal = (JUPITER/100) * earth_weight
    elif planet.upper() == "SATURN":
        planet_cal = (SATURN/100) * earth_weight
    elif planet.upper() == "URANUS":
        planet_cal = (URANUS/100) * earth_weight
    elif planet.upper() == "NEPTUNE":
        planet_cal = (NEPTUNE/100) * earth_weight
    else:
        print("Invalid planet name.")
    

    planet_cal = round(planet_cal, 2)

    print(f"Weight on {planet} is {planet_cal}")



if __name__ == "__main__":
    main()