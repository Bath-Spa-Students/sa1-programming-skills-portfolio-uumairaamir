def check_even_odd(number):
    """Function to determine if a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    # Ask the user for a number
    user_input = int(input("Enter a number: "))
    
    # Get the result
    result = check_even_odd(user_input)
    
    # Print the result
    print(result)

# Run the program
if __name__ == "__main__":
    main()