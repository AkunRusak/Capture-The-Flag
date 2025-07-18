import base64

encoded = input("Masukkan string base64: ")
decoded = base64.b64decode(encoded).decode()
print("Decoded:", decoded)