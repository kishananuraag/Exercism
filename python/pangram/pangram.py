from string import ascii_lowercase

alphabets = set(ascii_lowercase)

def is_pangram(sentence):
    return alphabets.issubset(sentence.lower())    
