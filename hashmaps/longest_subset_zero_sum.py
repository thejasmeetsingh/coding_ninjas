def subsetSum(arr):
    if not arr:
        return 0
    
    max_length = 0
    hmap = dict()
    _sum = 0
    
    for idx in range(len(arr)):
        _sum += arr[idx]
    
        if _sum == 0:
            max_length = idx + 1
            
        if _sum in hmap:
            max_length = max(max_length, idx - hmap[_sum])
        hmap[_sum] = idx
    
    return max_length
