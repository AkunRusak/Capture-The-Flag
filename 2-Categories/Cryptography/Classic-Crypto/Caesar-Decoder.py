def caesar_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan
cipher = "Khoor Zruog"
for i in range(1, 26):
    print(f"Shift {i}: {caesar_decrypt(cipher, i)}")