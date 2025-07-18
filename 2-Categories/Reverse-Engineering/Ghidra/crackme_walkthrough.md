# 🔓 CrackMe Walkthrough with Ghidra

## 1. Buka Binary
- Import `easy-crackme` ke Ghidra
- Jalankan auto-analysis

## 2. Temukan Fungsi `main`
- Biasanya Ghidra mendeteksi `main()` otomatis
- Jika tidak, cari fungsi dengan banyak panggilan libc (e.g., `scanf`, `printf`)

## 3. Lacak Verifikasi Serial
- Cari string seperti `"Enter serial"` → lihat referensinya
- Telusuri fungsi yang membandingkan input user
- Biasanya ada `strcmp`, `strncmp`, atau perbandingan manual dengan `if (input[i] != x)`

## 4. Pahami Algoritma
- Gunakan "Decompile" untuk melihat C-like pseudo code
- Rename variabel untuk membantu pemahaman
- Komentar langkah-langkah penting

## 5. Temukan Serial / Bypass
- Dapatkan hasil serial valid atau patch kondisi supaya selalu benar
- Gunakan `Export Decompiled` untuk dokumentasi

🧠 Bonus:
- Tambahkan breakpoint lewat GDB untuk mengecek nilai runtime