import sys
import math

def is_prime(n):
    """Checks if a number is prime using an optimized method."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_pth_prime(p):
    """Finds the p-th prime number."""
    if p < 1:
        raise ValueError("Position must be a positive integer.")
    if p == 1:
        return 2
    
    count = 1
    num = 3
    while count < p:
        if is_prime(num):
            count += 1
        if count == p:
            break
        num += 2
    return num

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <p>")
        sys.exit(1)
    
    try:
        p_value = int(sys.argv[1])
        prime = get_pth_prime(p_value)
        print(f"The {p_value}-th prime is: {prime}")
    except ValueError as e:
        print(f"Error: Invalid input. Please provide a positive integer. Details: {e}")
        sys.exit(1)
