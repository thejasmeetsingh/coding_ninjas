def uniqueChar(s):
    new_string = ""
    _set = set()
    
    for char in s:
        if char not in _set:
            new_string += char
            _set.add(char)
    
    return new_string
