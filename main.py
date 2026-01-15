# Password Generator
import random

# Get user preferences
print("Welcome to the Password Generator!")

upper_case = input("Include uppercase letters? (y/n): ").lower() 
lower_case = input("Include lowercase letters? (y/n): ").lower()
numbers_included = input("Include numbers? (y/n): ").lower()
special_chars = input("Include special characters? (y/n): ").lower()

# Make sure at least one type is selected
while upper_case == 'n' and lower_case == 'n' and numbers_included == 'n' and special_chars == 'n':
    print("You must select at least one character type!")
    upper_case = input("Include uppercase letters? (y/n): ").lower() 
    lower_case = input("Include lowercase letters? (y/n): ").lower()
    numbers_included = input("Include numbers? (y/n): ").lower()
    special_chars = input("Include special characters? (y/n): ").lower()

#Initialize password with one guaranteed character from each selected type
password = []
if upper_case == 'y':
    password.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
if lower_case == 'y':
    password.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
if numbers_included == 'y':
    password.append(random.choice("01234567"))
if special_chars == 'y':
    password.append(random.choice("!@#$%^&*()-_=+[]{}|;:',.<>?/`~"))

# Count number of selected types
number_types = 0

if upper_case == 'y':
    number_types += 1
if lower_case == 'y':
    number_types += 1
if numbers_included == 'y':
    number_types += 1
if special_chars == 'y':
    number_types += 1

# Ask for password length and validate
password_length = int(input("Enter the desired password length: "))
while password_length < 7 or password_length < number_types:
    print(f"Password length must be at least 7 and at least {number_types} (number of selected types).")
    password_length = int(input("Enter the desired password length: "))

# Build allowed character pool
allowed_characters = ""
if upper_case == 'y':
    allowed_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if lower_case == 'y':
    allowed_characters += "abcdefghijklmnopqrstuvwxyz"
if numbers_included == 'y':
    allowed_characters += "0123456789"
if special_chars == 'y':
    allowed_characters += "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

# Fill remaining password length with random characters from the pool
remaining = password_length - len(password)
for _ in range(remaining):
    password.append(random.choice(allowed_characters))

# Shuffle to make it unpredictable
random.shuffle(password)

# Convert list to string and display
final_password = "".join(password)
print("Your password is:", final_password)

if len(final_password) > 12 and number_types >= 3:
    print("This is a strong password.")

elif len(final_password) >= 7 and number_types >= 2:
    print("This is a moderate password.")

else:
    print("This is a weak password. Consider using more character types or increasing the length.")
  