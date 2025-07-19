# picoCTF 2024 - Web Challenge: SQL Injection 💉

## 🔍 Deskripsi
Situs login rentan terhadap SQL Injection pada field `username`.

## 🧪 Payload yang digunakan

```sql
' OR 1=1 --
```

## 📋 Langkah-langkah

- Buka halaman login.
- Masukkan payload di kolom username, password bebas.
- Login berhasil → Flag muncul di dashboard admin.

## 🏁 Flag

`picoCTF{sql_injection_success}`


## 🛡️ Pembelajaran

- Pentingnya prepared statement.
- Jangan hanya filter `'`, validasi harus dilakukan di server.