from collections import Counter

text = input("Masukkan string: ")
frekuensi = Counter(text)
print("Frekuensi karakter:")
for char, count in frekuensi.items():
    print(f"{char}: {count}")