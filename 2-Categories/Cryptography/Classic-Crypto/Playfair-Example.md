# Playfair Cipher Example

## Kunci: MONARCHY

Matrix 5x5:

M O N A R
C H Y B D
E F G I/J K
L P Q S T
U V W X Z

## Contoh Enkripsi

Plaintext: `INSTRUMENTS`

1. IN → (I,N) → (G,O)  
2. ST → (S,T) → (Q,T)  
3. RU → (R,U) → (D,M)  
4. ME → (M,E) → (C,O)  
5. NT → (N,T) → (Q,R)  
6. SX → (S,X) → (T,Z)

Ciphertext: **GOQTDMCOQRTZ**

---

## Aturan Umum

- Gunakan pasangan huruf
- Jika huruf sama, tambahkan 'X'
- Ganti 'J' dengan 'I'
- Gunakan kotak Playfair 5x5 untuk substitusi
