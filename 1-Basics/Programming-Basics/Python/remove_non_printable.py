text = input("Masukkan teks dengan karakter aneh: ")
cleaned = ''.join([c for c in text if c.isprintable()])
print("Hasil bersih:", cleaned)