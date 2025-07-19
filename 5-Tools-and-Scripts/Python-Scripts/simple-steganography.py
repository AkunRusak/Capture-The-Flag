# ============================================
# SIMPLE STEGANOGRAPHY (LSB)
# ============================================
def hide_text_in_binary(cover_text, secret_text):
    # Simple example - hide secret in LSB of ASCII values
    binary_secret = ''.join(format(ord(char), '08b') for char in secret_text)
    binary_secret += '1111111111111110'  # Delimiter
    
    result = []
    secret_index = 0
    
    for char in cover_text:
        if secret_index < len(binary_secret):
            ascii_val = ord(char)
            # Replace LSB with secret bit
            new_ascii = (ascii_val & 0xFE) | int(binary_secret[secret_index])
            result.append(chr(new_ascii))
            secret_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

def extract_text_from_binary(stego_text):
    binary_data = ''
    for char in stego_text:
        binary_data += str(ord(char) & 1)
    
    # Find delimiter
    delimiter = '1111111111111110'
    end_index = binary_data.find(delimiter)
    
    if end_index != -1:
        secret_binary = binary_data[:end_index]
        secret_text = ''
        for i in range(0, len(secret_binary), 8):
            byte = secret_binary[i:i+8]
            if len(byte) == 8:
                secret_text += chr(int(byte, 2))
        return secret_text
    
    return "No hidden message found"

# Usage
# cover = "This is a cover text for hiding secret message"
# secret = "FLAG{hidden}"
# stego = hide_text_in_binary(cover, secret)
# extracted = extract_text_from_binary(stego)
# print(f"Extracted: {extracted}")