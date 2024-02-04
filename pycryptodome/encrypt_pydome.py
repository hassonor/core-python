# Import necessary modules from PyCryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Define the key used for AES encryption. Ensure it's either 16, 24, or 32 bytes long
# for AES-128, AES-192, or AES-256, respectively.
key = b'mysecretpassword'  # 16 byte password

# Generate a random Initialization Vector (IV) of size equal to AES block size (16 bytes).
# The IV is used for ensuring unique ciphertexts even if the same plaintext is encrypted multiple times.
iv = get_random_bytes(AES.block_size)

# Create a new AES cipher object in CBC mode with the given key and IV.
cipher = AES.new(key, AES.MODE_CBC, iv)

# Define the plaintext message to be encrypted.
# In practice, this could be input from a user, read from a file, etc.
plaintext = b'this is my super secret message to encrypt'

# Pad the plaintext to make its length a multiple of the block size, then encrypt it.
# Padding is required for messages that aren't a multiple of block size.
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Print the IV and ciphertext. In real applications, these would need to be safely stored or transmitted.
print("IV:", iv)            # 128 bit
print("Ciphertext:", ciphertext)  # Encrypted data (will be a multiple of block_size)

# Open a file in binary write mode. The file will contain the IV followed by the ciphertext.
# This is a common way to store them together since both are needed for decryption.
with open('cipher_file', 'wb') as c_file:
    # Write the IV to the file. Although the IV does not need to be kept secret like the key,
    # it is essential for the decryption process and must be the same as the one used during encryption.
    c_file.write(cipher.iv)
    # Write the ciphertext to the file after the IV.
    c_file.write(ciphertext)
