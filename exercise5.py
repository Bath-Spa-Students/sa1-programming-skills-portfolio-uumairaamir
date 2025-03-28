# Function to get the number of days in a month
def get_days_in_month(month, year=None):
    # Dictionary mapping month numbers to the number of days
    month_days = {
        1: 31,  # January
        2: 28,  # February (default)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31, # October
        11: 30, # November
        12: 31  # December
    }
    
    # Check if the month is valid
    if month in month_days:
        days = month_days[month]
        # Check for leap year if the month is February
        if month == 2 and year is not None:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days = 29  # Leap year adjustment
        return days
    else:
        return None  # Invalid month

# Main program
def main():
    # Ask the user for the month number
    month = int(input("Enter the month number (1-12): "))
    
    # Check if the month is February to ask for the year
    if month == 2:
        year = int(input("Enter the year: "))
        days = get_days_in_month(month, year)
    else:
        days = get_days_in_month(month)
    
    # Output the result
    if days is not None:
        print(f"There are {days} days in month {month}.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")

# Run the program
if __name__ == "__main__":
    main()