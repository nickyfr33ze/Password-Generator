# Author: Nick Friesen
# Date: 2024-04-31
# Description: A simple Python program that generates a random password of a user-specified length for the command line.
# Usage: Run 'python3 CLI.py' in the command line and follow the prompts to generate a password.
# Please see the README.md file for more information for the web GUI.

import random
import sys
import time
from random_word import RandomWords # type: ignore
chars = '' # All usable characters determined by the user
everything = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_+-=,./<>?;:[]'
lower = 'abcdefghijklmnopqrstuvwxyz' # Lowercase letters
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Uppercase letters
numbers = '0123456789' # Numbers
symbols = '!@#$%^&*()_+-=,./<>?;:[]' # Symbols
password = '' # The generated password

# Ask the user if they would like to create a passphrase or a password
# Else/If statement to determine. If the user wants a passphrase, have them enter yes or 'y'. If no, have them enter no or 'n'.
def generate_passphrase():
    num_words = int(input("Enter the number of random words for the passphrase: ")) # Get user input for number of words
    delimiter = input("Enter the delimiter to use between words: ") # Get user input for delimiter
    passphrase = delimiter.join([RandomWords().get_random_word() for _ in range(num_words)]) # Generate the passphrase
    print("\nPassphrase generated!") # Print a message to let the user know the passphrase has been generated
    time.sleep(0.5) # Wait for half a second
    print(passphrase) # Print the passphrase
    print("")
    time.sleep(0.5) # Wait for half a second
    print("Please consider using a password manager to store your passphrase(s) securely.") # Print a message asking the user to securely store their passphrase.
    print("----------------------------------------")
    sys.exit() # Exit the program

# Function to generate the password
def generate_password():
    for i in range(length): 
        # Loop through the length of the password
        password += random.choice(chars) # Add a random character to the password
    print("\nPassword generated!") # Print a message to let the user know the password has been generated
    time.sleep(0.5) # Wait for half a second
    print(password) # Print the password
    print("")
    time.sleep(0.5) # Wait for half a second
    print("Please consider using a password manager to store your password(s) securely.") # Print a message asking the user to securely store their password.
    print("----------------------------------------")

# Ask the user if they would like to generate a passphrase instead of a password. Will run the generate_passphrase() function if the user enters 'y' or 'yes'.
passphraseQuestion = input(str("Would you like to generate a passphrase instead of a password? (y/n): "))
if passphraseQuestion == 'y' or passphraseQuestion == 'yes':
    generate_passphrase()
elif passphraseQuestion == 'n' or passphraseQuestion == 'no':
    print("Generating a password instead.")
    time.sleep(1)
length = int(input("Enter the desired password length: ")) # Get user input for password length

# Check if the password length is less than 16 prior to prompting for more info. Exits the program if less than 16.
if (length < 16):
    # If the password length is less than 16, print a warning
    print("----------------------------------------")
    time.sleep(1) # Wait for 1 second
    print("[*] WARNING: Passwords shorter than 16 characters are not recommended.")
    time.sleep(2) # Wait for 2 seconds
    print("[*] Please consider using a longer password.")
    time.sleep(1.5) # Wait for 1.5 seconds
    print("")
    time.sleep(1) # Wait for 1 second
    print("[*] This program will now exit. Re-run 'python3 CLI.py' to try again.")
    time.sleep(2) # Wait for 2 seconds
    print("----------------------------------------")
    sys.exit() # Exit the program

# Ask if the user wants to add all the letters, numbers, and special characters to their password without having to go through each prompt.
everythingQuestion = input("Do you want to include all letters, numbers, and special characters in your password? (y/n): ")
if everythingQuestion == 'y':
    chars += everything
    time.sleep(1)

elif everythingQuestion != 'y':
    time.sleep(1)
    print("----------------------------------------")
    time.sleep(0.5)
    print("Please answer each prompt below.")
    time.sleep(0.5)
    # Asking the user what letters, numbers, and symbols they want in their passwords and adds them to the 'chars' variable
    lowerQuestion = input("Do you want lowercase letters in your password? (y/n): ") # Ask the user if they want lowercase letters
    if lowerQuestion == 'y': # If the user wants lowercase letters
        chars += lower # Add lowercase letters to the list of possible characters
    time.sleep(0.5) # Wait for half a second
    upperQuestion = input("Do you want uppercase letters in your password? (y/n): ") # Ask the user if they want uppercase letters
    if upperQuestion == 'y': # If the user wants uppercase letters
        chars += upper # Add uppercase letters to the list of possible characters
    time.sleep(0.5) # Wait for half a second
    numberQuestion = input("Do you want numbers in your password? (y/n): ") # Ask the user if they want numbers
    if numberQuestion == 'y': # If the user wants numbers
        chars += numbers # Add numbers to the list of possible characters
    time.sleep(0.5) # Wait for half a second
    specialCharQuestion = input("Do you want special characters in your password? (y/n): ") # Ask the user if they want special characters
    if specialCharQuestion == 'y': # If the user wants special characters
        chars += symbols # Add symbols to the list of possible characters
    time.sleep(0.5) # Wait for half a second
print("----------------------------------------")
time.sleep(1) # Wait for 1 second
print("Generating password...") # Print a message to let the user know the password is being generated
time.sleep(2) # Wait for 2 seconds
generate_password() # Generate the password