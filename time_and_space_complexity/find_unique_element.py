def findUnique(arr, n):
    if not arr:
        return -1
    
    if len(arr) == 1:
        return arr[0]
    
    arr.sort()
    
    if arr[0] != arr[1]:
        return arr[0]
    
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
            return arr[i]
        
    return arr[-1]
