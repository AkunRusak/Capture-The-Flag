#!/bin/bash
read -p "Masukkan bilangan biner (misal 1010): " bin
echo "Desimal: $((2#$bin))"
