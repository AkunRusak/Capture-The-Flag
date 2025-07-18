# 🔍 Binary Analysis Intro

Reverse Engineering dalam CTF sering kali berfokus pada analisa file biner untuk memahami logika internalnya tanpa source code.

## 📌 Tools Umum
- **Ghidra**: Decompiler open-source dari NSA
- **IDA Free / IDA Pro**: GUI disassembler yang populer
- **Radare2 / Cutter**: Powerful dan open-source
- **objdump / strings / ltrace / strace**: CLI tools dasar

## 📂 Tujuan Analisis
- Mencari hardcoded flag / password
- Memahami alur logika aplikasi
- Menemukan kerentanan seperti buffer overflow
- Mengubah perilaku program tanpa source code

---

## 🛠️ Teknik Umum
1. **Static Analysis**
   - Tanpa mengeksekusi file
   - Gunakan IDA, Ghidra, `objdump`, `strings`

2. **Dynamic Analysis**
   - Dengan menjalankan program
   - Gunakan `gdb`, `ltrace`, `strace`, atau debugger GUI

3. **Patching Binary**
   - Mengubah instruksi dalam binary (cth: je → jmp)

---

## 🧠 Tips
- Mulailah dari `main()` function
- Perhatikan string yang muncul
- Lihat syscall dan input-output
- Gunakan breakpoints untuk menelusuri alur