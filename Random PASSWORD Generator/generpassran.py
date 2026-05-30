import random
import string

def generate_password(length=12):
    # Combine characters: lowercase + uppercase + digits + punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choice
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a 16-character password
new_password = generate_password(16)
print(f"Generated Password: {new_password}")
