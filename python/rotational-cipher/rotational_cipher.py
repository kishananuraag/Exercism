from string import ascii_lowercase as chars
def rotate(text, key):
    cipher = chars[key:] + chars[:key]
    mapper = str.maketrans(chars + chars.upper(), cipher+cipher.upper())
    return text.translate(mapper)
    
