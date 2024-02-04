# Author: Nick Friesen
# Date: 2024-02-04
# Description: A simple Python program that generates a random password of a user-specified length for the command line.
# Usage: Run 'python3 CLI.py' in the command line and follow the prompts to generate a password.
# Please see the README.md file for more information for the web GUI.

import random
import sys
import time
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=,./<>?;:[]\|' # All possible characters
password = '' # The generated password
length = int(input("Enter the desired password length: ")) # Get user input for password length

if (length < 16): 
    # If the password length is less than 16, print a warning
    print("----------------------------------------")
    print("Warning: Passwords shorter than 16 characters are not recommended.")
    print("Please consider using a longer password.")
    print("")
    print("This program will now exit. Re-run 'python3 gen.py' to try again.")
    print("----------------------------------------")
    sys.exit() # Exit the program

elif (length >= 16):
    print("----------------------------------------")
    print("Generating password...") # Print a message to let the user know the password is being generated
    time.sleep(2) # Wait for 2 seconds
    
    for i in range(length): 
        # Loop through the length of the password
        password += random.choice(chars) # Add a random character to the password
    print("\nPassword generated!") # Print a message to let the user know the password has been generated
    print(password) # Print the password
    print("")
    print("Please consider using a password manager to store your password(s).") # Print a message asking the user to securely store their password.
    print("----------------------------------------")

else:
    print("An error occurred. Please try again.") # Print an error message if something goes wrong
