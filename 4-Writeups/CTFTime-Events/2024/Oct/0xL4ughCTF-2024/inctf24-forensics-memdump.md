# 🧠 InCTF 2024 - Forensics Memory Dump

## 📦 File: `memdump.raw`

Pertama, gunakan Volatility3 untuk mengidentifikasi OS profile.

```bash
vol -f memdump.raw windows.info
```
Setelah itu, `pslist` dan `cmdline` digunakan untuk melihat aktivitas proses.


## 🔍 Temuan

- Proses `notepad.exe` aktif
- File bernama `flag.txt` muncul dalam `filescan`
- Dump file dengan offset tertentu → ditemukan flag
```bash
vol -f memdump.raw windows.filescan
vol -f memdump.raw windows.dumpfiles -Q 0x12345678 -D dump/
```


✅ Flag ditemukan di dump file:
```bash
INCTF{memdump_flag_3xtr4cted}
```