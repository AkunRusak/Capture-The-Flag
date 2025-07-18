#!/bin/bash

TARGET=$1

echo "[*] Checking FTP access on $TARGET ..."
ftp -inv $TARGET <<EOF
user anonymous anonymous
ls
bye
EOF