def number_to_words(n):
    """Convert a number to words."""
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + ones[n % 10]
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + "hundred"
        else:
            return ones[n // 100] + "hundredand" + number_to_words(n % 100)
    elif n == 1000:
        return "onethousand"
    return ""

def total_letters(limit):
    total = 0
    for i in range(1, limit + 1):
        total += len(number_to_words(i))
    return total

# Calculate the total letters used for numbers from 1 to 1000
result = total_letters(1000)
print(f"Total letters used: {result}")
