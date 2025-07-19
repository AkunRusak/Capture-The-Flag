# ============================================
# MAIN FUNCTION FOR TESTING
# ============================================
def main():
    print("CTF Python Scripts Collection")
    print("=" * 40)
    
    # Example usage of some functions
    print("\n1. Base64 Example:")
    encoded = b64_encode("CTF{example_flag}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {b64_decode(encoded)}")
    
    print("\n2. Caesar Cipher Example:")
    cipher_results = caesar_bruteforce("FWDI")[:5]  # Show first 5 results
    for result in cipher_results:
        print(result)
    
    print("\n3. Hash Example:")
    generate_hashes("password")
    
    print("\n4. Morse Code Example:")
    morse = text_to_morse("SOS")
    print(f"SOS in Morse: {morse}")
    print(f"Decoded: {morse_to_text(morse)}")

if __name__ == "__main__":
    main()