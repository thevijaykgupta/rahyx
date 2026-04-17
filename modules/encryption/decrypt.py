from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

def decrypt_message(encrypted):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted).decode()