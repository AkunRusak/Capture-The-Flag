# 🧠 Setting Up Ghidra for Reverse Engineering

## 📥 Install Ghidra
1. Download dari [ghidra-sre.org](https://ghidra-sre.org)
2. Ekstrak ZIP-nya
3. Jalankan `ghidraRun` (Linux/macOS) atau `ghidraRun.bat` (Windows)

## 📁 Membuka Project
- File → New Project → Non-Shared Project
- Drag & drop binary (ELF/EXE) ke dalam project
- Klik kanan → “Analyze” → OK

## ⚙️ Tips Ghidra
- Gunakan **Function Graph** untuk visualisasi alur
- Rename fungsi/variabel agar lebih mudah dibaca
- Tambahkan komentar: tekan `;` pada baris
- Untuk rename: tekan `L` (label)

> 🔐 Jangan lupa simpan secara berkala, Ghidra tidak autosave.