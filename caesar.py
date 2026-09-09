import random

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Test karne ke liye
if __name__ == "__main__":
    while True:
        message = input("\nEnter text (or 'exit' to quit): ")
        if message.lower() == "exit":
            print("Bye!")
            break

        shift = random.randint(1, 25)
        print("Random Shift Value:", shift)

        encrypted = caesar_encrypt(message, shift)
        print("Encrypted:", encrypted)

        decrypted = caesar_decrypt(encrypted, shift)
        print("Decrypted:", decrypted)