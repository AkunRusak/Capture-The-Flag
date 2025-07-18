escaped = input("Masukkan string Unicode escaped (misal \\u0048\\u0069): ")
print("Decoded:", bytes(escaped, "utf-8").decode("unicode_escape"))