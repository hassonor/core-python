# AES encryption (EAX mode: authenticated encryption mode)
# Recommended mode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

with open('aes_eax_key', 'wb') as f:
    f.write(key)

cipher = AES.new(key, AES.MODE_EAX)

with open('rsa_key.bin', 'rb') as f:
    data = f.read()

e_data, tag = cipher.encrypt_and_digest(data)  # Both Encryption and Authentication

with open('rsa_key_enc', 'wb') as f:
    f.write(cipher.nonce)
    f.write(tag)
    f.write(e_data)
