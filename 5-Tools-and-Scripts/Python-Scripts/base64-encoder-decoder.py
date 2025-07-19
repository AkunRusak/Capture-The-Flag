# ============================================
# BASE64 ENCODER/DECODER
# ============================================
import base64

def b64_encode(data):
    return base64.b64encode(data.encode()).decode()

def b64_decode(data):
    try:
        return base64.b64decode(data).decode()
    except:
        return "Invalid Base64"

# Usage
# print(b64_encode("Hello World"))
# print(b64_decode("SGVsbG8gV29ybGQ="))