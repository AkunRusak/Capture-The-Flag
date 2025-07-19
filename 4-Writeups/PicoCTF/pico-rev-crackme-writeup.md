# picoCTF - Reverse Challenge: CrackMe 🔍

## 🔧 Tools Used
- Ghidra
- strings
- xxd

## 💡 Analisa
- Binary meminta input berupa serial.
- Validasi dilakukan dengan loop dan XOR.
- Output benar jika hasil XOR = nilai konstan.

## 🧠 Solusi
Reverse algoritma XOR dengan Ghidra → ubah menjadi Python.

## 📜 Script
```python
serial = ''
key = [0x33, 0x55, 0x21, 0x77]
for i in range(12):
    serial += chr(key[i % 4] ^ target[i])
print(serial)
```

## 🏁 Flag

`picoCTF{rev_success_1234}`