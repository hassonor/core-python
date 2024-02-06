from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

with open('rsa_private.pem') as f:
    private_key = f.read()

key = RSA.importKey(private_key)
cipher = PKCS1_OAEP.new(key)

with open('messageToSend.enc', 'rb') as f:
    e_data = f.read()

data = cipher.decrypt(e_data)

with open('messageToSendDecrypted.txt', 'w') as f:
    f.write(data.decode())
