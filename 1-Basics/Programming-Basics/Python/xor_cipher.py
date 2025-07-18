text = input("Masukkan teks: ")
key = 13
print("Hasil XOR:")
print(''.join([chr(ord(c) ^ key) for c in text]))