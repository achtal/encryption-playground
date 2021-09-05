# simple cipher found in a puzzle book
# encryption method:
# swap last letter of word with first letter of following word for entire plain text
# punctuation is ignored
# case remains

"""
example:
plain text
The quick, brown fox jumps over the lazy dog

encrypted
Thq euicb, krowf noj xumpo svet rhl eazd yog
"""


def substitution_cipher(text):
    cipher_text = ''
    # break text into words
    words = text.split(' ')
    # loop through words and swap first and last letters
    for i in range(len(words)):
        if i == 0:
            # first word only swaps last letter
            new_word = words[i][:-1] + words[i+1][:1]
            cipher_text += new_word
        elif i == len(words) - 1:
            new_word = ' ' + words[i-1][-1:] + words[i][1:]
            cipher_text += new_word
        else:
            new_word = ' ' + words[i-1][-1:] + words[i][1:-1] + words[i+1][:1]
            cipher_text += new_word
    return cipher_text

