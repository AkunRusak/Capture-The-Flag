text = input("Masukkan teks: ")
shifts = [1, 2, 3, 4, 5]  # shift bisa disesuaikan
result = ''
for i, c in enumerate(text):
    if c.islower():
        result += chr((ord(c) - 97 + shifts[i % len(shifts)]) % 26 + 97)
    else:
        result += c
print("Hasil Shift:", result)