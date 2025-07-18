#!/bin/bash

TARGET=$1

echo "[*] Enum SMB shares on $TARGET ..."
smbclient -L //$TARGET -N

echo "[*] Try null session ..."
smbclient //"$TARGET"/share -N