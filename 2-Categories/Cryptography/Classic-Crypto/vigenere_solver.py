from itertools import cycle

def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    for c, k in zip(ciphertext, cycle(key)):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            p = (ord(c.lower()) - ord(k.lower())) % 26
            plaintext += chr(p + base)
        else:
            plaintext += c
    return plaintext

# Contoh penggunaan
cipher = "Lxfopv ef rnhr"
key = "lemon"
print(vigenere_decrypt(cipher, key))