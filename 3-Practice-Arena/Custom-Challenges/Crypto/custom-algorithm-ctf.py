# Custom CTF crypto logic generator (untuk tantangan lanjutan)

def encrypt_custom(msg, key):
    result = []
    key = key.upper()
    for i, c in enumerate(msg):
        if c.isalpha():
            k = ord(key[i % len(key)]) - ord('A')
            if c.isupper():
                result.append(chr((ord(c) - ord('A') + k) % 26 + ord('A')))
            else:
                result.append(chr((ord(c) - ord('a') + k) % 26 + ord('a')))
        else:
            result.append(c)
    return ''.join(result)

if __name__ == "__main__":
    msg = "This is your secret challenge. Good luck!"
    key = "REVERSECIPHER"
    enc = encrypt_custom(msg, key)
    print("Encrypted:", enc)