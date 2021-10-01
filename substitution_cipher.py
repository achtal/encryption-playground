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
import string


def substitution_cipher(text):
    # handle punctuation in text
    punct_dict = {}
    # for punctuation found assign location to a dictionary
    for x in string.punctuation:
        punct_dict[x] = [n for n in range(len(text)) if text.find(x, n) == n]

    # remove punctuation before applying cipher
    text_no_punct = ''.join([char for char in text if char not in string.punctuation])
    
    cipher_text = ''
    # break text into words
    words = text_no_punct.split(' ')
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
            
    # put punctuation back into string
    for i in punct_dict.keys():
        for place in punct_dict[i]:
            cipher_text = cipher_text[:place] + i + cipher_text[place:]
            
    return cipher_text

