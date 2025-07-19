# ============================================
# VIGENERE CIPHER
# ============================================
def vigenere_encrypt(plaintext, key):
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += encrypted_char
            key_index += 1
        else:
            result += char
    
    return result

def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in ciphertext.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += decrypted_char
            key_index += 1
        else:
            result += char
    
    return result

# Usage
# encrypted = vigenere_encrypt("HELLO", "KEY")
# print(f"Encrypted: {encrypted}")
# print(f"Decrypted: {vigenere_decrypt(encrypted, 'KEY')}")