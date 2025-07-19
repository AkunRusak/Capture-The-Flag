#!/bin/bash
# Extract files from PCAP
echo "[*] Extracting files from $1"
tcpflow -r $1
