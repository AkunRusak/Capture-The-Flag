# ============================================
# XOR CIPHER
# ============================================
def xor_cipher(data, key):
    result = ""
    for i, char in enumerate(data):
        result += chr(ord(char) ^ ord(key[i % len(key)]))
    return result

def xor_bruteforce_single_byte(data):
    results = []
    for key in range(256):
        try:
            result = ''.join(chr(ord(char) ^ key) for char in data)
            if all(32 <= ord(c) <= 126 for c in result):
                results.append(f"Key {key} ({chr(key)}): {result}")
        except:
            continue
    return results

# Usage
# encrypted = xor_cipher("Hello", "key")
# decrypted = xor_cipher(encrypted, "key")
# print(f"Encrypted: {encrypted}")
# print(f"Decrypted: {decrypted}")