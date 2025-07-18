# SHA Hashing Overview

SHA (Secure Hash Algorithm) digunakan untuk menghasilkan hash dari input data. Hash bersifat satu arah dan tidak dapat dibalik.

---

## Jenis SHA Umum

| Algoritma | Output |
|-----------|--------|
| SHA-1     | 160-bit |
| SHA-256   | 256-bit |
| SHA-512   | 512-bit |

---

## Contoh Python (SHA-256)

```python
import hashlib

text = b"CTF is fun"
hashed = hashlib.sha256(text).hexdigest()
print("SHA-256:", hashed)