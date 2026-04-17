from modules.encryption.encrypt import generate_key, encrypt_message
from modules.encryption.decrypt import decrypt_message
from modules.steganography.embed import embed_data
from modules.steganography.extract import extract_data

# STEP 1: Generate key (only once)
generate_key()

# STEP 2: Input message
message = "This is a secret message"

# STEP 3: Encrypt
encrypted = encrypt_message(message)
encrypted_str = encrypted.decode()

# STEP 4: Embed
embed_data("data/input_images/input.png", encrypted_str, "data/output_images/stego.png")

print("Data embedded successfully!")

# STEP 5: Extract
extracted = extract_data("data/output_images/stego.png")

# STEP 6: Decrypt
original = decrypt_message(extracted.encode())

print("Recovered Message:", original)