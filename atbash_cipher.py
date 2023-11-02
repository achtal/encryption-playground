"""
The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: 
A <=> Z; B <=> Y; C <=> X; etc.

Capitalisation is retained and non alphabetic characters (punctuation etc.) is not altered

example:
Plaintext:  Hello world!
Ciphertext: Svool dliow!
"""

import string


def atbash(txt):
    # load ascii into lists
    lc = [c for c in string.ascii_lowercase]
    uc = [c for c in string.ascii_uppercase]

    # convert to dictionaries
    lc_d = dict([(k, v) for i, (k, v) in enumerate(zip(lc, lc[::-1]))])
    uc_d = dict([(k, v) for i, (k, v) in enumerate(zip(uc, uc[::-1]))])

    # combine dictionaries
    d = dict(lc_d.items() | uc_d.items())

    cipher = ''

    # encrypt txt
    for c in txt:
        try:
            cipher += f'{d[c]}'
        except KeyError:
            cipher += c

    return cipher
  
