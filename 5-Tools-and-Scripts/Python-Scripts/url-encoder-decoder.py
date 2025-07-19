# ============================================
# URL ENCODER/DECODER
# ============================================
import urllib.parse

def url_encode(text):
    return urllib.parse.quote(text)

def url_decode(encoded_text):
    return urllib.parse.unquote(encoded_text)

# Usage
# encoded = url_encode("Hello World!")
# print(f"Encoded: {encoded}")
# print(f"Decoded: {url_decode(encoded)}")
