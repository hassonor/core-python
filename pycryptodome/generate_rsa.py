from Crypto.PublicKey import RSA

# Define a passphrase that will be used to encrypt your private key.
# This adds a layer of security. The private key will require this passphrase to be decrypted.
secret_code = "SomeSecretCodeDontTellAnyone"

# Generate a new RSA key pair. The number (2048) specifies the modulus size in bits.
# A size of 2048 bits is generally considered sufficient for security.
key = RSA.generate(2048)

# Encrypt and export the private key using the specified passphrase.
# The PKCS#8 standard is used for storing the key (pkcs=8).
# The private key is encrypted using a combination of scrypt (a password-based key derivation function)
# and AES128-CBC (a symmetric encryption algorithm with a 128-bit key, using Cipher Block Chaining mode).
encrypted_key = key.export_key(passphrase=secret_code,
                               pkcs=8,
                               protection="scryptAndAES128-CBC",
                               prot_params={'iteration_count': 131072})  # scrypt iteration count

# Write the encrypted private key to a binary file.
# The key is binary data, so the file is opened in binary write mode ('wb').
with open("aes/cbc_encrypt_decrypt/rsa_key.bin", "wb") as f:
    f.write(encrypted_key)

# Extract the public key from the key pair and export it.
# The public key can be shared openly and is used for encrypting messages or verifying signatures.
# The corresponding private key is kept secret and is used for decrypting messages or creating signatures.
public_key = key.public_key().export_key()

# Print the public key.
# The public key is exported in the default format (PEM) and can be easily shared.
print(public_key)
