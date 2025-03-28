# Function to get user input and handle potential errors
def get_user_input():
    # Get user input for name, hometown, and age
    name = input("Please enter your full name: ")
    hometown = input("Please enter your hometown: ")
    
    # Loop until a valid integer is entered for age
    while True:
        age_input = input("Please enter your age: ")
        try:
            age = int(age_input)  # Try to convert the input to an integer
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")

    return name, hometown, age

# Main program
def main():
    # Get user input
    name, hometown, age = get_user_input()
    
    # Store the information
    biography = {
        "Name": name,
        "Hometown": hometown,
        "Age": age
    }
    
    # Print the values on separate lines using a single print() statement
    print("\n".join(f"{key}: {value}" for key, value in biography.items()))

# Run the program
if __name__ == "__main__":
    main()