def caesar_decrypt(text, shift):
    result = ''
    for char in text:
        if char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

for i in range(26):
    print(f"{i}: {caesar_decrypt('khoor zruog', i)}")