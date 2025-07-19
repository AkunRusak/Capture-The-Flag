# 🔓 Personal Web Auth Bypass Test

## 🧪 Target
Simulasi login form sederhana dengan validasi PHP dan SQLite backend.

## 🧠 Tujuan
Menguji kekuatan filter input dan potensi SQL Injection di parameter username/password.

## 🛠️ Injection Payload

```sql
admin' OR 1=1 --
```
- Disisipkan dalam input `username`, hasilnya:
- Login berhasil tanpa password yang benar.
- Menunjukkan validasi tidak menggunakan parameter binding (`prepare`).


## ✅ Mitigasi

- Gunakan parameterized queries.
- Validasi input di sisi server dengan regex whitelist.