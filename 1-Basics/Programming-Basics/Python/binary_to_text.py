binary = input("Masukkan biner (contoh: 01001000 01101001): ").split()
text = ''.join([chr(int(b, 2)) for b in binary])
print("Hasil:", text)