from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)
public_key = key.publickey()

# Encryption
message = b"Hello from RSA!"
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)
print("Encrypted:", ciphertext.hex())

# Decryption
decipher = PKCS1_OAEP.new(key)
plaintext = decipher.decrypt(ciphertext)
print("Decrypted:", plaintext.decode())