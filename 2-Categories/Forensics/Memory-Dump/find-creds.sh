#!/bin/bash

# Script to extract potential credentials from memory dump strings

if [ -z "$1" ]; then
  echo "Usage: $0 memory-dump.raw"
  exit 1
fi

echo "[*] Extracting strings..."
strings "$1" > dump_strings.txt

echo "[*] Searching for keywords: password, passwd, pwd, login, key"
grep -Ei 'pass(word)?|pwd|login|key' dump_strings.txt | tee found_creds.txt
