#!/bin/bash
# Automate gdb with predefined commands
BINARY=$1
echo "[*] Attaching gdb to $BINARY"
gdb -q $BINARY -ex "set disassembly-flavor intel" -ex "break main" -ex "run"
