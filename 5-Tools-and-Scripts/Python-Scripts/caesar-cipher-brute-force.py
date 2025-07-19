# ============================================
# CAESAR CIPHER BRUTE FORCE
# ============================================
def caesar_bruteforce(ciphertext):
    results = []
    for i in range(26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - base - i) % 26 + base)
            else:
                decrypted += char
        results.append(f"Shift {i}: {decrypted}")
    return results

# Usage
# for result in caesar_bruteforce("KHOOR ZRUOG"):
#     print(result)