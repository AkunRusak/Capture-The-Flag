# ============================================
# FREQUENCY ANALYSIS
# ============================================
from collections import Counter

def frequency_analysis(text):
    text = text.upper().replace(' ', '')
    counter = Counter(char for char in text if char.isalpha())
    total = sum(counter.values())
    
    print("Frequency Analysis:")
    for char, count in counter.most_common():
        percentage = (count / total) * 100
        print(f"{char}: {count} ({percentage:.1f}%)")
    
    return counter

# Usage
# frequency_analysis("HELLO WORLD")