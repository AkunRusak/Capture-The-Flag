# 🛡️ Anti-Debugging Checks

Beberapa CrackMe atau binary di CTF menyisipkan mekanisme anti-debugger untuk menghalangi reverse engineering. Berikut beberapa teknik umum yang perlu diwaspadai:

## 🔍 Teknik Umum

### 1. `IsDebuggerPresent()` (Windows)
```c
if (IsDebuggerPresent()) {
    exit(1);
}

---

### 2. Timing Checks
Mengukur waktu antar instruksi untuk mendeteksi breakpoints:
```c
start = GetTickCount();
// some logic
end = GetTickCount();
if (end - start > threshold) {
    exit(1);
}

---

### 3. Trap Flag (TF) dan INT 3

Memanfaatkan instruksi `int 3` dan `0xCC` sebagai jebakan.