def findDuplicate(arr, n):
    if not arr:
        return -1
    
    prev = -1
    arr.sort()
    
    for element in arr:
        if prev == element:
            return element
        prev = element
    
    return -1
  
