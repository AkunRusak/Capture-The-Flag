hex_str = input("Masukkan string heksadesimal (contoh: 68656c6c6f): ")
ascii_str = bytes.fromhex(hex_str).decode()
print("Hasil ASCII:", ascii_str)