import math

# Calculate 10!
factorial_10 = math.factorial(1000)

# Convert the result to a string and sum the digits
sum_of_digits = sum(int(digit) for digit in str(factorial_100))

# Print the result
print(f"The sum of the digits in 10! is: {sum_of_digits}")
