# ============================================
# JWT TOKEN DECODER
# ============================================
import json

def decode_jwt(token):
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return "Invalid JWT format"
        
        header = parts[0]
        payload = parts[1]
        signature = parts[2]
        
        # Add padding if needed
        header += '=' * (4 - len(header) % 4)
        payload += '=' * (4 - len(payload) % 4)
        
        decoded_header = json.loads(base64.b64decode(header).decode())
        decoded_payload = json.loads(base64.b64decode(payload).decode())
        
        result = {
            'header': decoded_header,
            'payload': decoded_payload,
            'signature': signature
        }
        
        return json.dumps(result, indent=2)
        
    except Exception as e:
        return f"Error decoding JWT: {str(e)}"

# Usage
# jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
# print(decode_jwt(jwt))