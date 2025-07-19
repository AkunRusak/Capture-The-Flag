# ============================================
# BINARY CONVERTER
# ============================================
def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    try:
        binary = binary.replace(' ', '')
        text = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            text += chr(int(byte, 2))
        return text
    except:
        return "Invalid binary string"

# Usage
# print(text_to_binary("Hi"))
# print(binary_to_text("0100100001101001"))