# Classical Cipher Toolkit 🔐

A Python-based command-line tool implementing classical cryptographic ciphers — Caesar and Vigenère — along with cryptanalysis (cipher-breaking) capabilities using frequency analysis.

## Why This Project?

Understanding classical ciphers builds intuition for modern encryption. This tool demonstrates both encrypting/decrypting text and breaking ciphers without knowing the key, combining programming skills with analytical/statistical thinking — core skills for cryptography and security roles.

## Features

- **Caesar Cipher** — Encrypt and decrypt text using a shift-based substitution cipher
- **Vigenere Cipher** — Encrypt and decrypt text using a keyword-based polyalphabetic cipher (stronger than Caesar)
- **Caesar Cipher Cracker** — Breaks Caesar-encrypted text *without knowing the key*, using chi-squared statistical frequency analysis against standard English letter frequencies
- **Unified CLI Menu** — Single entry point (`main.py`) to access all features

## How It Works

### Caesar Cipher

Each letter is shifted by a fixed number of positions in the alphabet (the "key"). For example, with shift 3: A → D, B → E, etc.

### Vigenere Cipher

Uses a repeating keyword where each letter of the keyword determines a different shift value for the corresponding letter of the plaintext — making it significantly harder to break than Caesar with simple frequency analysis.

### Frequency Analysis Cracking

English text has a predictable letter-frequency distribution (E, T, A, O, I, N... being most common). The cracker tries all 26 possible shifts, scores each resulting decryption using a chi-squared statistic against expected English letter frequencies, and returns the shift with the best statistical match — no key required.

## Tech Stack

- Python 3
- Built-in libraries only: `collections`, `random`

## Project Structure

cipher-toolkit/
├── caesar.py # Caesar cipher encrypt/decrypt

├── vigenere.py # Vigenère cipher encrypt/decrypt

├── frequency_analysis.py # Chi-squared based Caesar cracker

├── main.py # CLI menu — unified entry point

└── README.md


## How to Run

1. Clone the repository:
 git clone https://github.com/Rachittyagi791/cipher-toolkit.git cd cipher-toolkit


2. Run the tool: 
python main.py


3. Choose an option from the menu:
   
1.Caesar Encrypt

2.Caesar Decrypt

3.Vigenere Encrypt

4.Vigenere Decrypt

5.Crack Caesar (Frequency Analysis)

6.Exit



## Example

Choose an option (1-6): 1

Enter text: Attack at dawn

Random Shift Value: 7

Encrypted: Haaphr ha khcu



Choose an option (1-6): 5

Enter encrypted text to crack: Haaphr ha khcu

Guessed Shift: 7

Decrypted Text: Attack at dawn 



## What This Project Demonstrates

- Classical cipher algorithm implementation from scratch
- Statistical cryptanalysis (chi-squared frequency analysis)
- Clean, modular Python code (separated into reusable modules)
- Understanding of why modern encryption (AES, RSA) replaced classical ciphers — resistance to statistical attacks

## Future Improvements

- Vigenère cipher cracking using Kasiski Examination (key-length detection)
- Web-based UI using Flask/Streamlit

## Author

Rachit Tyagi
