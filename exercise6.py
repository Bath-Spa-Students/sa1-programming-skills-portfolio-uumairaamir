# Define the correct password
correct_password = "12345"
# Set the maximum number of attempts
max_attempts = 5
# Initialize the attempt counter
attempts = 0

# Use a while loop to repeatedly ask for the password
while attempts < max_attempts:
    # Ask the user to enter the password
    user_input = input("Enter the password: ")
    
    # Check if the entered password is correct
    if user_input == correct_password:
        print("Access granted!")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1  # Increment the attempt counter
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")
        
# If the maximum number of attempts is reached
if attempts == max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")