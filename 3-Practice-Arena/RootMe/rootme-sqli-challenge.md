# RootMe Challenge - SQL Injection

## 🔎 Target
http://challenge01.root-me.org/web-serveur/ch16/

## 🎯 Tujuan
Dump data dari database menggunakan SQL injection di form login.

## 💥 Payload Awal
```sql
admin' OR '1'='1
```

## 🧠 Langkah:

1. Tes dengan payload dasar seperti ' OR 1=1--.
2. Cek error feedback → blind atau verbose?
3. Gunakan ORDER BY dan UNION SELECT untuk mapping kolom.
4. Dapatkan users dan passwords.


## 📌 Tips:

- Gunakan BurpSuite untuk intercept form.
- Perhatikan URL redirect.


## 🏁 Flag

```
ROOTME{sql_injection_mastered}
```