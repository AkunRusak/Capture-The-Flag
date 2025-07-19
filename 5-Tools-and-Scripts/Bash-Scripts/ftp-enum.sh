#!/bin/bash
# Usage: ./ftp-enum.sh <target>
TARGET=$1
echo "[*] Enumerating FTP on $TARGET"
nmap -p 21 --script=ftp-anon,ftp-bounce,ftp-syst $TARGET
