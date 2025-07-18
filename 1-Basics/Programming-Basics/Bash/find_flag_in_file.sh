#!/bin/bash
if grep -q "FLAG" secret.txt; then
  echo "✅ Flag ditemukan:"
  grep "FLAG" secret.txt
else
  echo "❌ Flag tidak ditemukan."
fi
