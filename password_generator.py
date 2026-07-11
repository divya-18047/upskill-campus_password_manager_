import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*"

characters = letters + numbers + symbols

password = ""

for i in range(12):
    password += random.choice(characters)

print("Generated Password:", password)