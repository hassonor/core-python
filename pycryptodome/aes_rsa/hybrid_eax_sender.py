from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Create a random AES symmetric key
aes_key = get_random_bytes(16)  # 16 bytes = 128bit encryption

# Get recipients public rsa key
with open('recipient_rsa_public.pem', 'rb') as f:
    pub_key = f.read()
rsa_key = RSA.importKey(pub_key)
rsa_cipher = PKCS1_OAEP.new(rsa_key)
enc_aeskey = rsa_cipher.encrypt(aes_key)

# Use AES key to encrypt file (AES symmetric)
with open('recipe.txt', 'rb') as f:
    data = f.read()

aes_cipher = AES.new(aes_key, AES.MODE_EAX)
enc_data, tag = aes_cipher.encrypt_and_digest(data)

# Write both encrypted AES key and encrypted file to one bundled file
with open('bundle.enc', 'wb') as f:
    f.write(enc_aeskey)  # 256 bytes
    f.write(aes_cipher.nonce)  # 16 bytes
    f.write(tag)  # 16 bytes
    f.write(enc_data)
