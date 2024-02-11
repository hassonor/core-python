# Usage: python3 hybrid_sender.py publicKey fileToEncrypt fileToSend

import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

if len(sys.argv) != 4:
    print(f"Usage: python {sys.argv[0]} publicKey fileToEncrypt fileToSend")
    sys.exit()

# Create a random AES symmetric key
aes_key = get_random_bytes(16)  # 16 bytes = 128bit encryption

# Get the recipients public RSA Key
with open(sys.argv[1], "rb") as f:
    public_key = f.read()
rsa_key = RSA.importKey(public_key)
rsa_cipher = PKCS1_OAEP.new(rsa_key)
enc_aes_key = rsa_cipher.encrypt(aes_key)

# Use AES key to encrypt file (AES symmetric)
with open(sys.argv[2], 'rb') as f:
    data = f.read()

aes_cipher = AES.new(aes_key, AES.MODE_EAX)
enc_data, tag = aes_cipher.encrypt_and_digest(data)

# Writ both encrypted AES key and encrypted file to one bundled file
with open(sys.argv[3], 'wb') as f:
    f.write(enc_aes_key)  # 256 bytes
    f.write(aes_cipher.nonce)  # 16 bytes
    f.write(tag)  # 16 bytes
    f.write(enc_data)
