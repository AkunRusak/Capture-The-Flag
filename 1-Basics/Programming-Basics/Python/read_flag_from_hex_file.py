with open("hex_flag.txt", "r") as f:
    hex_data = f.read().strip()
    decoded = bytes.fromhex(hex_data).decode()
    print("Isi flag:", decoded)