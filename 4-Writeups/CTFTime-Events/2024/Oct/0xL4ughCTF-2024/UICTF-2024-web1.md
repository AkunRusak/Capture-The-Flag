# 🕸️ UICTF 2024 - Web Challenge 1 Writeup

## 🎯 Challenge: Simple Login Panel

Kita diberikan halaman login sederhana. Source HTML mengindikasikan penggunaan `POST` ke `/login.php`. Setelah beberapa tes dan burp repeater, ditemukan bahwa SQL Injection sederhana bisa digunakan.

### 🔎 Payload

```sql
' OR 1=1 --
```


### ✅ Solusi

Kita masukkan payload ke field username, password apapun → login sukses.
Flag: `UICTF{bl1nd_sql_work5!}`