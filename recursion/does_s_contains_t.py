def contains(s,t):
    if not t:
        return True
    
    if not s:
        return False
    
    if s[0] == t[0]:
        t = t[1:]
    s = s[1:]
    
    res = contains(s, t)
    return res
  
