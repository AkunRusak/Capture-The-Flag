
---

### 📄 `modern_crypto_quiz.pdf`

**[Isi tidak ditampilkan karena ini adalah file PDF]**  
(Silakan simpan sebagai file `modern_crypto_quiz.pdf`. Bisa berisi soal pilihan ganda terkait RSA, AES, hashing, dan Elliptic Curve.)

---


```markdown
# Pengenalan Elliptic Curve Cryptography (ECC)

ECC adalah bentuk kriptografi kunci publik yang menggunakan struktur matematis kurva eliptik.

---

## Bentuk Umum Kurva

y² = x³ + ax + b mod p

Contoh kurva: secp256k1 (digunakan dalam Bitcoin)

---

## Keunggulan ECC

- Kunci lebih kecil dibanding RSA untuk tingkat keamanan yang sama
- Lebih efisien untuk perangkat dengan sumber daya terbatas
- Banyak digunakan dalam TLS, blockchain, dan sistem mobile

---

## Operasi Dasar

- Point Addition
- Point Doubling
- Scalar Multiplication (k * G)

---

## Python Example (using `ecdsa`)

```python
from ecdsa import SigningKey, NIST256p

sk = SigningKey.generate(curve=NIST256p)
vk = sk.get_verifying_key()

message = b"secure message"
signature = sk.sign(message)

print("Signature:", signature.hex())
print("Verification:", vk.verify(signature, message))
