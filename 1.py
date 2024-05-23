import secrets
import string

def generate_password(length=16):
    if length < 4:  # Minimum length to ensure all character types are included
        raise ValueError("Password length should be at least 4")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "[]{}()*;/,._-"

    # Ensure the password contains at least one of each character type
    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from the combined pool
    all_characters = lower + upper + digits + symbols
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the list to avoid predictable patterns and then join into a string
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# Example usage
length = 16  # You can specify any length here
password = generate_password(length)
print(password)
