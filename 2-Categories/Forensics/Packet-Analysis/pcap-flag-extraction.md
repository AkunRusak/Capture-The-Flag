# Panduan Ekstraksi Flag dari File PCAP

## 1. Buka File PCAP di Wireshark

- Gunakan fitur **Follow TCP Stream** untuk melihat alur komunikasi
- Filter umum:
  - `http`
  - `tcp contains "flag"`
  - `ftp-data` untuk FTP file transfer
  - `frame contains "CTF"`

---

## 2. Ekstraksi Data Manual

- Klik kanan pada stream → Follow Stream → Save As...
- Ubah encoding bila perlu: ASCII, Raw, atau Hex Dump
- Periksa file upload/download, credentials, atau string mencurigakan

---

## 3. Ekstraksi Otomatis (Linux Tools)

```bash
# Ekstrak objek HTTP
tcpflow -r capture-challenge.pcap

# Ekstrak file dari PCAP
wireshark → File > Export Objects > HTTP

---

## 4. Cek DNS Exfiltration

- Filter: `dns`
- Cek subdomain mencurigakan, payload di dalam nama domain
- Lihat pola Base64 atau hex dalam query

## 5. Tools Alternatif

- `tshark` (CLI Wireshark)
- `scapy` (Python)
- `NetworkMiner`
- `Zeek` / `Bro`


---

### 📄 `malware-exfiltration.py`

```python
from scapy.all import *

def dns_exfil_detect(pcap_file):
    packets = rdpcap(pcap_file)
    for pkt in packets:
        if pkt.haslayer(DNSQR):
            query = pkt[DNSQR].qname.decode()
            if any(x in query.lower() for x in ['flag', 'ctf', 'exfil']):
                print(f"[!] Suspicious DNS Query: {query}")

dns_exfil_detect("dns-exfiltration.pcap")
