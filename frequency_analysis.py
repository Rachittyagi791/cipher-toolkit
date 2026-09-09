from collections import Counter
from caesar import caesar_decrypt

ENGLISH_FREQ = {
    'A': 8.2, 'B': 1.5, 'C': 2.8, 'D': 4.3, 'E': 12.7, 'F': 2.2,
    'G': 2.0, 'H': 6.1, 'I': 7.0, 'J': 0.15, 'K': 0.77, 'L': 4.0,
    'M': 2.4, 'N': 6.7, 'O': 7.5, 'P': 1.9, 'Q': 0.095, 'R': 6.0,
    'S': 6.3, 'T': 9.1, 'U': 2.8, 'V': 0.98, 'W': 2.4, 'X': 0.15,
    'Y': 2.0, 'Z': 0.074
}

def chi_squared_score(text):
    letters_only = [c.upper() for c in text if c.isalpha()]
    total = len(letters_only)
    if total == 0:
        return float('inf')
    
    freq = Counter(letters_only)
    score = 0
    for letter in ENGLISH_FREQ:
        observed = freq.get(letter, 0)
        expected = ENGLISH_FREQ[letter] * total / 100
        if expected > 0:
            score += ((observed - expected) ** 2) / expected
    return score

def crack_caesar(ciphertext):
    best_shift = 0
    best_score = float('inf')
    best_text = ciphertext

    for shift in range(26):
        candidate = caesar_decrypt(ciphertext, shift)
        score = chi_squared_score(candidate)
        if score < best_score:
            best_score = score
            best_shift = shift
            best_text = candidate

    return best_shift, best_text


if __name__ == "__main__":
    while True:
        ciphertext = input("\nEnter encrypted text to crack (or 'exit' to quit): ")
        if ciphertext.lower() == "exit":
            print("Bye!")
            break

        guessed_shift, decrypted_text = crack_caesar(ciphertext)
        print(f"Guessed Shift: {guessed_shift}")
        print(f"Decrypted Text: {decrypted_text}")