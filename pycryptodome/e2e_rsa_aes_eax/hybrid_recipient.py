# Usage: python3 hybrid_recipient.py privateKey fileToDecrypt createdFile

import sys
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

if len(sys.argv) != 4:
    print(f"Usage: python {sys.argv[0]} privateKey fileToDecrypt createdFile")
    sys.exit()

with open(sys.argv[2], 'rb') as f:
    enc_aes_key = f.read(256)
    # 16 byte AES key becomes 156 bytes after RSA encryption
    nonce = f.read(16)
    tag = f.read(16)
    enc_data = f.read()

with open(sys.argv[1]) as f:
    private_key = f.read()

rsa_private_key = RSA.importKey(private_key)
rsa_cipher = PKCS1_OAEP.new(rsa_private_key)

aes_key = rsa_cipher.decrypt(enc_aes_key)

try:
    aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    data = aes_cipher.decrypt_and_verify(enc_data, tag)
except:
    print('Decryption of Authenticity failure')

with open(sys.argv[3], 'wb') as f:
    f.write(data)
