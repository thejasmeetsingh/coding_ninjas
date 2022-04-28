def printIntersection(arr1, n1, arr2, n2):
    if not arr1 or not arr2:
        return
    
    hmap = dict()
    
    for element in arr1:
        hmap[element] = hmap.get(element, 0) + 1
    
    for element in arr2:
        if hmap.get(element, 0) != 0:
            print(element)
            hmap[element] -= 1
