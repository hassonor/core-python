# AES CBC decryption

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open('enc_data', 'rb') as f:
    iv = f.read(16)  # read the iv on the top of file (16 bytes)
    e_data = f.read()  # read the rest of the file's data

with open('aeskey', 'rb') as f:
    key = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)  # Here we specify the 'iv' (we don't want it to be generated automatically)

data = cipher.decrypt(e_data)
data = unpad(data, AES.block_size)  # reverse order

with open('dec_data', 'wb') as f:
    f.write(data)
