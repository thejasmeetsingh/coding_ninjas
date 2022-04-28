def pairSum0(arr, n):
    if not arr:
        return
    
    hmap = dict()
    count = 0
    
    for element in arr:
        if hmap.get(-element, 0) != 0:
            count += hmap[-element]
        hmap[element] = hmap.get(element, 0) + 1
    
    return count
