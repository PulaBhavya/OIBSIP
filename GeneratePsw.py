import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters  # a-z + A-Z
    if use_numbers:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&*() etc.

    if not characters:
        return "No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if length <= 0:
        print("Please enter a positive length.")
    else:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Enter numeric value for length.")
