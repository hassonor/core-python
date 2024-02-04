# Import necessary modules from PyCryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Define the key used for AES encryption and decryption.
# Ensure it's either 16, 24, or 32 bytes long for AES-128, AES-192, or AES-256.
key = b'mysecretpassword'

# Open the file containing the ciphertext (encrypted data) in binary read mode.
with open('cipher_file', 'rb') as c_file:
    # Read the first 16 bytes from the file which represent the initialization vector (IV).
    # It's essential for the AES CBC mode and should be the same as used during encryption.
    iv = c_file.read(16)
    # Read the rest of the file which contains the ciphertext.
    ciphertext = c_file.read()

# Create a new AES cipher object in CBC mode with the given key and IV.
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext and then remove padding to get the original plaintext.
# The same block size used during encryption must be used for unpadding.
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

# Decode the plaintext bytes object to a string and print it.
# Assuming the original plaintext was a string, it was encoded to bytes for encryption,
# so now we decode it back to a string.
print(plaintext.decode())  # Original message
