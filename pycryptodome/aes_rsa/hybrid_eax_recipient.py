from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

with open('bundle.enc', 'rb') as f:
    enc_aeskey = f.read(256)  # 16 byte AES key becomes 256 bytes (2048bits) after RSA encryption
    nonce = f.read(16)
    tag = f.read(16)
    enc_data = f.read()

with open('recipient_rsa_private.pem') as f:
    key = f.read()

private_key = RSA.importKey(key)
rsa_cipher = PKCS1_OAEP.new(private_key)

aes_key = rsa_cipher.decrypt(enc_aeskey)
try:
    aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    data = aes_cipher.decrypt_and_verify(enc_data, tag)
except:
    print('Decryption or Authenticity failure')

with open('recipe_decrypted.txt', 'wb') as f:
    f.write(data)
