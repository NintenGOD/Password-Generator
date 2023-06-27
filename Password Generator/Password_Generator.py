
import random
import string

def generate_password(length=8):
    """
    Generates a random password with the specified length.

    Parameters:
        length (int): The length of the password. Default is 8.

    Returns:
        str: The generated password.
    """
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by selecting random characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Usage example
length = 12
password = generate_password(length)
print("Generated Password:", password)
