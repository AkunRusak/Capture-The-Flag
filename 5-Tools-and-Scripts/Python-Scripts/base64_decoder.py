import base64

encoded = input("Enter base64 string: ")
try:
    decoded = base64.b64decode(encoded).decode()
    print(f"Decoded string: {decoded}")
except Exception as e:
    print(f"Decoding error: {e}")