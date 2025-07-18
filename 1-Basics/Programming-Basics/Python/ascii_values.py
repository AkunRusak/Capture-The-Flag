text = input("Masukkan teks: ")
print("Nilai ASCII per karakter:")
for char in text:
    print(f"{char} -> {ord(char)}")