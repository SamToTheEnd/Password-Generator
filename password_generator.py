import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if numbers:
        characters += digits

    if special_characters:
        characters += special_chars


    password = []

    if numbers:
        password.append(random.choice(digits))

    if special_characters:
        password.append(random.choice(special_chars))

    while len(password) < min_length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password[:min_length])


min_length = int(input("Please enter the minimum length of password: "))
contains_number = input("Do you want numbers? (y/n): ").lower() == "y"
contains_special_character = input("Do you want special characters? (y/n): ").lower() == "y"

password = generate_password(min_length, contains_number, contains_special_character)

print("Here is your password:", password)
