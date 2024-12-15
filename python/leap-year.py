def is_leap_year(year):
    """Check if a given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

def count_sundays():
    """Count the Sundays that fell on the 1st of the month during the 20th century."""
    # Starting on January 1, 1901 (which is a Tuesday, so day_of_week is 2)
    day_of_week = 2  # 0 = Sunday, 1 = Monday, 2 = Tuesday, ..., 6 = Saturday
    sunday_count = 0

    # Iterate over each year from 1901 to 2000
    for year in range(1901, 2001):
        # Iterate over each month in the year
        for month in range(1, 13):
            # Check if the first of the month is a Sunday
            if day_of_week == 0:  # Sunday
                sunday_count += 1

            # Update the day_of_week for the next month
            if month in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
                day_of_week = (day_of_week + 31) % 7
            elif month in [4, 6, 9, 11]:  # Months with 30 days
                day_of_week = (day_of_week + 30) % 7
            else:  # February, 28 or 29 days
                if is_leap_year(year):
                    day_of_week = (day_of_week + 29) % 7
                else:
                    day_of_week = (day_of_week + 28) % 7

    return sunday_count

# Call the function and print the result
result = count_sundays()
print(f"Number of Sundays that fell on the 1st of the month: {result}")
