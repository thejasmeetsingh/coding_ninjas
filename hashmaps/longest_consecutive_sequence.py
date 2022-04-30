def longestConsecutiveSubsequence(arr,n): 
    if not arr:
        return []
    
    max_length = -1
    start = 0
    
    hmap = {el: True for el in arr}
    
    for element in arr:
        if hmap[element]:
            _max_length = 0
            
            current = element
            while current in hmap:
                hmap[current] = False
                current += 1
                _max_length += 1
            
            current = element - 1
            while current in hmap:
                hmap[current] = False
                current -= 1
                _max_length += 1
                
            if _max_length > max_length:
                max_length = _max_length
                start = current + 1
            elif _max_length == max_length:
                for _element in arr:
                    if _element == current + 1:
                        start = current + 1
                        break
                    elif _element == start:
                        break
    
    return start, (start + max_length) - 1
