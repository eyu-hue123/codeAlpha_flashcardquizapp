from cryptography.fernet import Fernet

# Generate and save your key (run once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load key
def load_key():
    return open("key.key", "rb").read()

# Encrypt data
def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

# Decrypt data
def decrypt_data(token):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()
