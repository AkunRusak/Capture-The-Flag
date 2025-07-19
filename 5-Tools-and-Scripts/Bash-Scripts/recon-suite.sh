#!/bin/bash
# Recon automation script
TARGET=$1
echo "[+] Starting full recon on $TARGET"
nmap -T4 -A -oN recon_$TARGET.txt $TARGET
whatweb $TARGET > whatweb_$TARGET.txt
gobuster dir -u http://$TARGET -w /usr/share/wordlists/dirb/common.txt -o gobuster_$TARGET.txt
