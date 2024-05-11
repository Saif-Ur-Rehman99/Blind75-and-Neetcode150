# tokenization ! and & are words <-- confuse model

import string

print(string.punctuation)
# text = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

punc = string.punctuation

def remove_punctuation(text):
    for char in punc:
        text = text.replace(char, '')
    return text


def remove_punc(text):
    return text.translate(str.maketrans('','', punc))


text = "string doesn't in'clude this colon"

print(remove_punc(text))