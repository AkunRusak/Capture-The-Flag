# ============================================
# DIRECTORY BRUTE FORCER
# ============================================
import requests
from urllib.parse import urljoin

def directory_bruteforce(base_url, wordlist, extensions=['']):
    found_directories = []
    
    for word in wordlist:
        for ext in extensions:
            url = urljoin(base_url, word + ext)
            try:
                response = requests.get(url, timeout=3)
                if response.status_code == 200:
                    print(f"Found: {url} (Status: {response.status_code})")
                    found_directories.append(url)
                elif response.status_code in [301, 302]:
                    print(f"Redirect: {url} (Status: {response.status_code})")
                    found_directories.append(url)
            except requests.exceptions.RequestException:
                continue
    
    return found_directories

# Usage (example wordlist)
# common_dirs = ['admin', 'login', 'dashboard', 'config', 'backup', 'test', 'dev']
# extensions = ['', '.php', '.html', '.txt', '.bak']
# directory_bruteforce("http://example.com/", common_dirs, extensions)