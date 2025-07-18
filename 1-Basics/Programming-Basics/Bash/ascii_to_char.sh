#!/bin/bash
read -p "Masukkan kode ASCII (misal 72): " ascii
printf "\\$(printf '%03o' "$ascii")\n"
