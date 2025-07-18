codes = input("Masukkan list kode Unicode (contoh: 72 101 108 108 111): ").split()
text = ''.join([chr(int(c)) for c in codes])
print("Hasil:", text)