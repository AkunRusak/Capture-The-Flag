# 📷 QR Code Challenge Analysis

## Step-by-step Decode:

1. **ZBar Tool**
   - Use `zbarimg` to extract plain text from image:
     ```
     zbarimg qr-challenge.png
     ```

2. **Check for Multilayer**
   - Jika hasil terlihat tidak masuk akal, bisa jadi:
     - Gambar QR mengandung QR di dalam QR
     - Gambar QR dibuat transparan sebagian
     - Layer QR di-*overlay*

3. **Check for File Embedding**
   - Cek apakah PNG menyimpan data selain gambar:
     ```
     binwalk -e qr-challenge.png
     strings qr-challenge.png | grep FLAG
     ```

4. **Stego Technique**
   - QR code dengan noise atau manipulasi visual bisa membutuhkan filter:
     - Gunakan kontras tinggi
     - Crop manual bagian penting
     - Gunakan `steghide`, `zsteg`, atau `qrtools`

5. **Hex Dump**
   - Jika QR ternyata adalah base64/data URI:
     ```
     xxd qr-challenge.png
     ```

---

## Tools

- `zbarimg` (Linux)
- `qrtools`, `qreader`, `pyzbar` (Python)
- `CyberChef` untuk analisa lanjut