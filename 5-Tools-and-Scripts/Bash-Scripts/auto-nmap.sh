#!/bin/bash
# Usage: ./auto-nmap.sh <target>
TARGET=$1
echo "[*] Scanning target $TARGET"
nmap -sC -sV -oN initial_$TARGET.txt $TARGET
