def maxfreq(arr):
    if not arr:
        return
    
    _dict = dict()
    
    for element in arr:
        _dict[element] = _dict.get(element, 0) + 1
    
    max_count, max_key = 0, None

    for element in arr:
        if _dict[element] > max_count:
            max_count = _dict[element]
            max_key = element
    
    return max_key
