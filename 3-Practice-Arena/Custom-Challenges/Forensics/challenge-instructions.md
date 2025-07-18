# 🕵️ Custom Forensics Challenge - Practice Arena

Selamat datang di tantangan forensik custom! Tujuan dari tantangan ini adalah menemukan flag yang tersembunyi di berbagai jenis file digital.

## 📁 Disediakan File:
- 🧠 `memory-ctf.raw` → Dump memory dari sistem target
- 🧾 `pcap-challenge.pcap` → Traffic jaringan selama sesi CTF
- 🖼️ `stego-image-flag.png` → Gambar yang disusupi flag dengan teknik steganografi
- 🧪 `volatility-analysis.sh` → Script awal untuk menganalisis dump memory menggunakan Volatility
- 📄 `hidden-message.txt` → Potongan hasil analisis awal

## 🎯 Objective
Temukan flag tersembunyi di salah satu (atau lebih) dari file di atas. Flag menggunakan format umum: `CTF{...}`.

### 🧩 Petunjuk:
- Gunakan Volatility Framework untuk dump memory
- Analisa trafik `pcap` menggunakan Wireshark atau `tshark`
- Gambar stego dapat dianalisis menggunakan `zsteg`, `steghide`, atau `binwalk`
- Buka `hidden-message.txt` untuk hint awal

Selamat berburu flag! 🎯