# TryHackMe - Blue Walkthrough

## 📌 Target Box: `BLUE`
IP: 10.10.10.40

## 🔍 Enumeration

### 🔹 Nmap
```bash
nmap -sC -sV -oN nmap-scan-results.txt 10.10.10.40
```

### 🔹 SMB Enum
```bash
smbclient -L //10.10.10.40
```
Terbuka share: `Users`, `Anonymous.`


## 🛠️ Exploitation

Menggunakan EternalBlue (MS17-010):
```bash
searchsploit eternalblue
```
Eksekusi exploit dengan `msfconsole`, hasilnya:
    - Reverse shell sebagai `NT AUTHORITY\SYSTEM`.


## 🧾 Privilege Escalation

Tidak diperlukan, sudah langsung root access.


## 🏁 Flag

```css
root.txt: THM{e7f84e472b6f...}
```