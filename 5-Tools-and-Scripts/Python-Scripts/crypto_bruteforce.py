alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_decrypt(cipher, shift):
    return ''.join(alphabet[(alphabet.index(c)-shift)%26] if c in alphabet else c for c in cipher.upper())

cipher = input("Enter ciphertext: ")
for shift in range(1, 26):
    print(f"Shift {shift}: {caesar_decrypt(cipher, shift)}")