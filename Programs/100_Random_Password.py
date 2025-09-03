# WAP to generate random password that contains symbols, numbers, characters
import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Test the function
password_length = 12
password = generate_password(password_length)
print("Generated Password:", password)
