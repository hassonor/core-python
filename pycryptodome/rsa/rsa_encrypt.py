from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

with open('rsa_public.pem') as f:
    public_key = f.read()

key = RSA.importKey(public_key)
cipher = PKCS1_OAEP.new(key)

with open('messageToSend.txt') as f:
    s = f.read().encode()

enc_data = cipher.encrypt(s)

with open('messageToSend.enc', 'wb') as f:
    f.write(enc_data)
