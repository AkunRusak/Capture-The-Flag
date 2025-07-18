# Panduan Dasar Steganografi Gambar

## 1. Teknik Umum Steganografi Gambar

- **LSB (Least Significant Bit)**: menyisipkan data di bit terakhir pixel
- **Metadata abuse**: menyisipkan data di EXIF atau header file
- **Color channel manipulation**: data tersembunyi di RGB channel tertentu
- **Appending file**: file atau zip disisipkan di akhir gambar

---

## 2. Tools yang Sering Digunakan

- `steghide`
- `zsteg`
- `binwalk`
- `strings`
- `exiftool`
- `stegsolve` (Java GUI)

---

## 3. Langkah Analisis Stego Gambar

```bash
# Cek metadata
exiftool hidden_flag.png

# Cari string mencurigakan
strings hidden_flag.png | less

# Lihat LSB RGB (gunakan stegsolve)

# Coba extract data tersembunyi
binwalk -e hidden_flag.png

# Cek menggunakan zsteg
zsteg hidden_flag.png

---

## 4. Tips

- Coba semua channel `(R/G/B/Alpha)` di stegsolve
- Periksa apakah gambar disisipi ZIP atau file lain
- Lihat perubahan pola warna pixel `(flag bisa berupa QR code tersembunyi)`