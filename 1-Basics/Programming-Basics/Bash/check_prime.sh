#!/bin/bash
read -p "Masukkan angka: " num
is_prime=1
for ((i=2; i<num; i++)); do
  if (( num % i == 0 )); then
    is_prime=0
    break
  fi
done
[[ $is_prime -eq 1 ]] && echo "$num adalah bilangan prima" || echo "$num bukan bilangan prima"
