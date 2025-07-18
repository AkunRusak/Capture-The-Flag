import codecs

text = input("Masukkan teks ROT13: ")
print("Hasil decoding:", codecs.decode(text, 'rot_13'))