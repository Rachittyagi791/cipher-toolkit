from math import gcd
from functools import reduce
from collections import Counter
from caesar import caesar_decrypt
from frequency_analysis import chi_squared_score


def find_repeated_sequences(ciphertext, seq_len=3):
    """Ciphertext mein repeated sequences aur unki positions dhoondo"""
    clean_text = "".join(c for c in ciphertext if c.isalpha()).upper()
    sequences = {}
    for i in range(len(clean_text) - seq_len):
        seq = clean_text[i:i+seq_len]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]
    return {k: v for k, v in sequences.items() if len(v) > 1}


def guess_key_length(ciphertext, max_length=15):
    """Repeated sequences ke distances ka GCD nikaal ke key length guess karo"""
    sequences = find_repeated_sequences(ciphertext)
    distances = []

    for positions in sequences.values():
        for i in range(1, len(positions)):
            distances.append(positions[i] - positions[i-1])

    if not distances:
        return 1  # fallback agar koi repeat na mile

    overall_gcd = reduce(gcd, distances)

    # GCD chhota ho sakta hai, isliye factors mein se best guess nikaalo
    if overall_gcd == 0 or overall_gcd > max_length:
        return 1

    return overall_gcd


def crack_vigenere_key(ciphertext, key_length):
    """Har column ko Caesar cipher ki tarah crack karke poori key banao"""
    clean_text = "".join(c for c in ciphertext if c.isalpha()).upper()
    key = ""

    for i in range(key_length):
        # Har key_length-th letter ek column banata hai
        column = clean_text[i::key_length]

        best_shift = 0
        best_score = float('inf')

        for shift in range(26):
            candidate = caesar_decrypt(column, shift)
            score = chi_squared_score(candidate)
            if score < best_score:
                best_score = score
                best_shift = shift

        # Shift se key letter nikaalo
        key += chr(best_shift + ord('A'))

    return key


def vigenere_decrypt_with_key(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result


def crack_vigenere(ciphertext):
    key_length = guess_key_length(ciphertext)
    key = crack_vigenere_key(ciphertext, key_length)
    decrypted = vigenere_decrypt_with_key(ciphertext, key)
    return key, decrypted


if __name__ == "__main__":
    while True:
        ciphertext = input("\nEnter Vigenère-encrypted text to crack (or 'exit' to quit): ")
        if ciphertext.lower() == "exit":
            print("Bye!")
            break

        key, decrypted = crack_vigenere(ciphertext)
        print(f"Guessed Key: {key}")
        print(f"Decrypted Text: {decrypted}")
        