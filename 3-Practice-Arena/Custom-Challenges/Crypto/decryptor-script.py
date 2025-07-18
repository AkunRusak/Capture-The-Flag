# Custom Vigenère decryptor
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for c in ciphertext:
        if c.upper() in ALPHABET:
            shift = ALPHABET.index(key[key_index % key_len])
            idx = ALPHABET.index(c.upper())
            plain_char = ALPHABET[(idx - shift) % 26]
            decrypted.append(plain_char if c.isupper() else plain_char.lower())
            key_index += 1
        else:
            decrypted.append(c)
    return ''.join(decrypted)

if __name__ == "__main__":
    with open("custom-vigenere-encrypted.txt") as f:
        encrypted = f.read()
    key = "REVERSECIPHER"
    print(vigenere_decrypt(encrypted, key))