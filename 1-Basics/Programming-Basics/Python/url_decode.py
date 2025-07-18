import urllib.parse

encoded = input("Masukkan string URL-encoded: ")
decoded = urllib.parse.unquote(encoded)
print("Hasil decoding:", decoded)