## Dynastic – Crypto Challenge 

## Challenge Overview 
We were given two files: 
- `output.txt` – contains the encrypted flag
- `source.py` – a Python script that encrypts the flag
- The goal was to **reverse engineer the encryption** and recover the original flag.

## Analysis 
1. **Inspect `output.txt`:** - The file contained the encrypted flag. It was clearly a **cipher**, not a hash, so it could be decrypted with the right logic.
2. **Inspect `source.py`:** - The script imports `FLAG` from a secret module. It uses two helper functions:
    ```python def to_identity_map(a): return ord(a) - 0x41  # A=0, B=1, ..., Z=25
    def from_identity_map(a): return chr(a % 26 + 0x41)  # reverse mapping

---
3. The encrypt function loops through each character: Alphabet characters are converted to a number (A=0…Z=25), added to the index, and converted back to a letter.
4. Finally, it writes the encrypted flag to output.txt.

## Solution path
- Understand the cipher: Each letter in the flag is shifted by its position index in the string. This is similar to a position-based Caesar cipher.
- Reverse the encryption: Create a decrypt function that subtracts the index from each letter instead of adding it
- Used a python script to decrypt the function which you can find [here](Dynastic.py)
- Save the python script using the command nano "filename.py"
- Run it using the command python3 filename.py
- Run this python script in the terminal to get the flag 

