def is_isogram(string):
    string_lower = [char for char in string.lower() if char.isalpha()]
    
    return len(set(string_lower)) == len(string_lower)
