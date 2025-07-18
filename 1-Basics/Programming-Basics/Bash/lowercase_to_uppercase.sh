#!/bin/bash
read -p "Masukkan teks: " teks
echo "$teks" | tr 'a-z' 'A-Z'
