import random
from caesar import caesar_encrypt, caesar_decrypt
from vigenere import vigenere_encrypt, vigenere_decrypt
from frequency_analysis import crack_caesar
from vigenere_crack import crack_vigenere


def menu():
    print("\n===== Classical Cipher Toolkit =====")
    print("1. Caesar Encrypt")
    print("2. Caesar Decrypt")
    print("3. Vigenère Encrypt")
    print("4. Vigenère Decrypt")
    print("5. Crack Caesar (Frequency Analysis)")
    print("6. Crack Vigenère (Kasiski Examination)")
    print("7. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            text = input("Enter text: ")
            shift = random.randint(1, 25)
            print("Random Shift Value:", shift)
            print("Encrypted:", caesar_encrypt(text, shift))

        elif choice == "2":
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            print("Decrypted:", caesar_decrypt(text, shift))

        elif choice == "3":
            text = input("Enter text: ")
            key = input("Enter keyword: ")
            print("Encrypted:", vigenere_encrypt(text, key))

        elif choice == "4":
            text = input("Enter text: ")
            key = input("Enter keyword: ")
            print("Decrypted:", vigenere_decrypt(text, key))

        elif choice == "5":
            text = input("Enter encrypted text to crack: ")
            shift, decrypted = crack_caesar(text)
            print(f"Guessed Shift: {shift}")
            print(f"Decrypted Text: {decrypted}")

        elif choice == "6":
            text = input("Enter Vigenère-encrypted text to crack: ")
            key, decrypted = crack_vigenere(text)
            print(f"Guessed Key: {key}")
            print(f"Decrypted Text: {decrypted}")

        elif choice == "7":
            print("Bye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()