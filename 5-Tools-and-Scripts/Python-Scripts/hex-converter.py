# ============================================
# HEX CONVERTER
# ============================================
def text_to_hex(text):
    return text.encode('utf-8').hex()

def hex_to_text(hex_string):
    try:
        return bytes.fromhex(hex_string).decode('utf-8')
    except:
        return "Invalid hex string"

# Usage
# print(text_to_hex("Hello"))
# print(hex_to_text("48656c6c6f"))