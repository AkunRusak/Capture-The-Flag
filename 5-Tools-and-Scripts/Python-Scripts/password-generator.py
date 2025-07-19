# ============================================
# PASSWORD GENERATOR
# ============================================
import random
import string

def generate_password(length=12, include_special=True):
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += "!@#$%^&*"
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_wordlist_passwords(base_words, variations=True):
    passwords = []
    
    for word in base_words:
        passwords.append(word)
        passwords.append(word.upper())
        passwords.append(word.lower())
        passwords.append(word.capitalize())
        
        if variations:
            # Add common number suffixes
            for i in range(10):
                passwords.append(f"{word}{i}")
                passwords.append(f"{word}0{i}")
            
            # Add common year suffixes
            for year in range(2020, 2026):
                passwords.append(f"{word}{year}")
            
            # Add common special character suffixes
            for char in "!@#$":
                passwords.append(f"{word}{char}")
    
    return list(set(passwords))  # Remove duplicates

# Usage
# print("Random password:", generate_password(16))
# base_words = ["password", "admin", "user", "test"]
# wordlist = generate_wordlist_passwords(base_words)
# print(f"Generated {len(wordlist)} password variations")