# ============================================
# ROT13/ROT-N CIPHER
# ============================================
def rot13(text):
    return text.encode('rot13')

def rot_n(text, n):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + n) % 26 + base)
        else:
            result += char
    return result

# Usage
# print(rot13("Hello World"))
# print(rot_n("Hello", 5))