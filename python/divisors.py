import math

# Function to calculate number of divisors of a number
def num_divisors(n):
    divisors = 1
    count = 0
    # Check for divisibility by all numbers up to sqrt(n)
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If i divides n, then both i and n/i are divisors
            if i == n // i:
                count += 1  # If it's a perfect square
            else:
                count += 2  # Otherwise, both i and n/i are distinct divisors
    return count

# Function to find the first triangle number with more than 500 divisors
def find_triangle_with_divisors(min_divisors):
    n = 1
    while True:
        # Calculate the n-th triangle number
        triangle_number = n * (n + 1) // 2
        # Check number of divisors
        if num_divisors(triangle_number) > min_divisors:
            return triangle_number
        n += 1

# Finding the first triangle number with more than 500 divisors
result = find_triangle_with_divisors(500)
print(result)
