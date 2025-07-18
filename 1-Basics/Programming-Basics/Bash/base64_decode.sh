#!/bin/bash
read -p "Masukkan string base64: " encoded
echo "$encoded" | base64 --decode
