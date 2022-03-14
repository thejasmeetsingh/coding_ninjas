def arrayRotateCheck(arr, n):
    if not arr:
        return 0
    
    prev = arr[0]
    
    for i in range(1, n):
        if prev > arr[i]:
            return i
    
    return 0
