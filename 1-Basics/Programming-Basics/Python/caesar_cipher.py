text = input("Masukkan teks: ")
shift = 3
encrypted = ''.join([chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() else c for c in text])
print("Hasil Caesar Cipher:", encrypted)