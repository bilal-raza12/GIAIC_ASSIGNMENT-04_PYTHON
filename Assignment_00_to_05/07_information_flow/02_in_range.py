def in_range(x, low, high):
    """Check if x is within the range [low, high]"""
    if x <= low and x >= high:
        return True
    else:
        return False
def main():
    num = int(input("\033[1mEnter a number: \033[0m"))
    low = int(input("\033[1mEnter the lower bound: \033[0m"))
    high = int(input("\033[1mEnter the upper bound: \033[0m"))
    print(f"Is {num} in range [{low}, {high}]? {in_range(num, low, high)}")