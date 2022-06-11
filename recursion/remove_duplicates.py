def removeConsecutiveDuplicates(s):
    if len(s) < 2:
        return s
    
    if s[0] != s[1]:
        return s[0]+removeConsecutiveDuplicates(s[1:])
    
    return removeConsecutiveDuplicates(s[1:])
