"""
example:
Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
"""
import string


def caesar_cipher(text, method, shift=-3):
    """
    A Caesar cipher implementation
    :param text: The text to be encrypted or decrypted
    :param shift: The shift to apply (default is -3) - can be positive or negative
    :param method: encrypt ("e") or decrypt ("d")
    :return: encrypted or decrypted text
    """
    ascii_ = {index: element for index, element in enumerate([x for x in string.ascii_uppercase])}
    cipher_text = ""

    for char in text:
        if char in string.punctuation or char in string.whitespace:
            cipher_text += char
        else:
            for key, value in ascii_.items():
                if char == value:
                    x = key

                    if method == "e":
                        cipher_text += (ascii_[(x + shift) % 26])
                    elif method == "d":
                        cipher_text += (ascii_[(x - shift) % 26])

    return cipher_text
