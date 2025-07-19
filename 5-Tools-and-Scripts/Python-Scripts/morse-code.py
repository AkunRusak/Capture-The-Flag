# ============================================
# MORSE CODE
# ============================================
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}

def text_to_morse(text):
    return ' '.join(MORSE_CODE.get(char.upper(), char) for char in text)

def morse_to_text(morse):
    words = morse.split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(REVERSE_MORSE.get(letter, letter) for letter in letters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

# Usage
# morse = text_to_morse("HELLO WORLD")
# print(f"Morse: {morse}")
# print(f"Text: {morse_to_text(morse)}")