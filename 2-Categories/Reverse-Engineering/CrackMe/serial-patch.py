from pwn import *

binary = ELF('./easy-crackme.exe')
patch_offset = 0x1234  # ganti sesuai alamat instruksi jne/jz

# Patch instruksi JNE (0x75) → JE (0x74)
with open('easy-crackme.exe', 'rb') as f:
    data = bytearray(f.read())

data[patch_offset] = 0x74

with open('crackme_patched.exe', 'wb') as f:
    f.write(data)

print("[+] Binary patched successfully.")
