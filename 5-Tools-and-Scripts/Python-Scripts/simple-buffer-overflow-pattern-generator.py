# ============================================
# SIMPLE BUFFER OVERFLOW PATTERN GENERATOR
# ============================================
def create_pattern(length):
    pattern = ""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(length):
        pattern += chars[i % len(chars)]
    
    return pattern

def find_offset(pattern, search_string):
    try:
        offset = pattern.index(search_string)
        return f"Offset found at position: {offset}"
    except ValueError:
        return "Pattern not found"

# Usage
# pattern = create_pattern(100)
# print(f"Pattern: {pattern}")
# print(find_offset(pattern, "EFGH"))