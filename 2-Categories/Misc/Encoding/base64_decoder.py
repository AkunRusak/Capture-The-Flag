import base64

# Ambil input dari file atau langsung dari string
with open("encoded_strings.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    try:
        decoded = base64.b64decode(line.strip()).decode('utf-8')
        print(f"[+] {line.strip()} → {decoded}")
    except Exception as e:
        print(f"[-] Failed to decode: {line.strip()} ({e})")