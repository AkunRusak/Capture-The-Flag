# 🖼️ VolgaCTF 2025 - Stego + Reverse

## 🎯 Soal

File gambar `.png` berisi flag tersembunyi. Tools yang disarankan: `zsteg`, `binwalk`, dan script custom.

## 📥 Langkah:

```bash
zsteg hidden.png
```

# LSB stego ditemukan di RGB, plane 0
→ Ekstrak hasilnya dan ditemukan skrip Python obfuscated.