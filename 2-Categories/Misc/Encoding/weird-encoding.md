# Catatan tentang Encoding Aneh di Dunia CTF

## 1. Jenis Encoding yang Sering Digunakan

- Base64 / Base32 / Base58 / Base85
- URL Encoding (percent encoding)
- Hex Encoding
- ASCII to Binary / Octal
- Unicode (obfuscated or emoji-style)
- Morse code
- Brainfuck / Base65536

---

## 2. Tips Identifikasi

- Ciri khas Base64: panjang kelipatan 4, huruf besar/kecil + angka + '='
- Hex: hanya 0-9 dan a-f, sering diawali '0x'
- URL: banyak '%20' atau '%xx'
- Unicode obfuscation: karakter aneh, emoji, atau simbol tak umum
- Jika terlihat normal tapi tak terbaca → bisa jadi UTF-16/32, ROT13, Zalgo, atau homoglyph

---

## 3. Tools Rekomendasi

- [CyberChef](https://gchq.github.io/CyberChef/)
- `base64`, `xxd`, `iconv`, `recode`
- Python: `codecs`, `base64`, `urllib.parse`, `binascii`

---

## 4. Contoh Analisis

```bash
# Decode base64
echo 'aGVsbG8gd29ybGQ=' | base64 -d

# Decode URL
echo '%68%65%6c%6c%6f' | xxd -r -p

# Convert hex to ASCII
echo '68656c6c6f' | xxd -r -p
