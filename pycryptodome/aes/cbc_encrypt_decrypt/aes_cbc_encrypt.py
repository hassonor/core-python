# AES CBC mode encryption
# AES CBC mode encryption provides confidentiality but not integrity.

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

with open('rsa_key.bin', 'rb') as f:
    data = f.read()

data = pad(data, AES.block_size)  # pad to 16 bytes

key = get_random_bytes(16)  # using 128bit encryption

# save aes key to aeskey file
with open('aeskey', 'wb') as f:
    f.write(key)

cipher = AES.new(key, AES.MODE_CBC)  # creates iv automatically

encrypted_data = cipher.encrypt(data)

with open('enc_data', 'wb') as f:
    f.write(cipher.iv)  # 16 bytes at the top of the file
    f.write(encrypted_data)
