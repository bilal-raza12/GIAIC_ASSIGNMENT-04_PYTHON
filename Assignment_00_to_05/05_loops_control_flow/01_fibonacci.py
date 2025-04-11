
# Fibonacci numbers are a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
MAX_TERM: int = 10000

def main():
    """
    This program prints the Fibonacci numbers up to a maximum term.
    
    """
    current: int = 0
    next: int = 1
    # The loop will continue until the current Fibonacci number is less than or equal to the maximum term.
    # The loop will print the current Fibonacci number and then update the current and next Fibonacci numbers.
    while current <= MAX_TERM: 
        print(current, end=", ")
        
        current , next = next ,  current + next
        assert current >= 0, "Fibonacci number is negative"

if __name__ == "__main__":
    main()