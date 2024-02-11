from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey()
public_key = key.publickey().exportKey()

with open('rsa_public.pem', 'wb') as f:
    f.write(public_key)

with open('rsa_private.pem', 'wb') as f:
    f.write(private_key)
