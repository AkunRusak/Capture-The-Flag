# ============================================
# HASH FUNCTIONS
# ============================================
import hashlib

def generate_hashes(text):
    data = text.encode()
    hashes = {
        'MD5': hashlib.md5(data).hexdigest(),
        'SHA1': hashlib.sha1(data).hexdigest(),
        'SHA256': hashlib.sha256(data).hexdigest(),
        'SHA512': hashlib.sha512(data).hexdigest()
    }
    
    for hash_type, hash_value in hashes.items():
        print(f"{hash_type}: {hash_value}")
    
    return hashes

# Usage
# generate_hashes("password123")