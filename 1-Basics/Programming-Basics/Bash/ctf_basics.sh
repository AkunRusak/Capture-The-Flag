#!/bin/bash

# ---------------------------
# CTF Programming-Basics Demo
# ---------------------------

echo "===[ CTF Programming Basics Start ]==="

# 1. Input dari pengguna
read -p "Masukkan nama kamu: " nama
echo "Halo, $nama! Selamat datang di CTF."

# 2. Operasi aritmatika
a=10
b=5
let hasil=$a+$b
echo "Contoh aritmatika: $a + $b = $hasil"

# 3. Loop sederhana
echo "Loop angka dari 1 sampai 5:"
for i in {1..5}
do
  echo "Angka: $i"
done

# 4. Cek file flag.txt
if [ -f "flag.txt" ]; then
  echo "✅ File flag.txt ditemukan!"
  echo "Isi flag: "
  cat flag.txt
else
  echo "❌ File flag.txt tidak ditemukan!"
fi

echo "===[ Selesai ]==="
