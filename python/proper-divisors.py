def sum_of_proper_divisors(n):
    divisors = [1]  # Start with 1 because 1 is a divisor of every number
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to sqrt(n)
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice
                divisors.append(n // i)
    return sum(divisors)

def find_amicable_numbers(limit):
    amicable_numbers = set()  # To store amicable numbers without duplicates
    for a in range(2, limit):
        b = sum_of_proper_divisors(a)
        if b != a and sum_of_proper_divisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    return sum(amicable_numbers)

# Find the sum of all amicable numbers under 10000
limit = 10000
result = find_amicable_numbers(limit)
print(f"The sum of all amicable numbers under {limit} is: {result}")
