# AES decryption (EAX mode)

from Crypto.Cipher import AES

with open('rsa_key_enc', 'rb') as f:
    nonce = f.read(16)  # Reading the nonce
    tag = f.read(16)  # Reading the tag
    e_data = f.read()  # Reading the rest of the data

with open('aes_eax_key', 'rb') as f:
    key = f.read()  # Read the key

try:
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(e_data, tag)
except ValueError:
    print('Decryption failed. Encrypted data possible tampered')

with open('rsa_key_dec', 'wb') as f:
    f.write(data)
