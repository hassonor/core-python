from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = b'mysecretpassword'  # 16 byte password

# Generate a random IV
iv = get_random_bytes(AES.block_size)

cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = b'this is my super secret message to encrypt'

# Pad the plaintext and then encrypt
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# IV is needed for decryption, so it should be stored or transmitted with the ciphertext
print("IV:", iv)            # 128 bit
print("Ciphertext:", ciphertext)  # Encrypted data (will be a multiple of block_size)

with open('cipher_file', 'wb') as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)
