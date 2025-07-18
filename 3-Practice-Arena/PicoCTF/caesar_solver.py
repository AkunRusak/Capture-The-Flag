# Caesar Cipher Solver
def decrypt(text, shift):
    decrypted = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

ciphertext = "Fdhvdu Flskhu lv vlpsoh"
for i in range(1, 26):
    print(f"[{i}] {decrypt(ciphertext, i)}")