import requests

base_url = input("Base URL (e.g., http://target.com/): ")
wordlist = ["admin", "login", "dashboard", ".git", "config"]

for word in wordlist:
    full_url = f"{base_url}/{word}"
    r = requests.get(full_url)
    if r.status_code == 200:
        print(f"[+] Found: {full_url}")