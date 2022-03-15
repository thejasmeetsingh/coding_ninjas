def maximumProfit(arr):
    if not arr:
        return 0
    
    _max = 0
    n = len(arr)
    arr.sort()
    
    for i in range(n):
        _max = max(_max, arr[i] * (n - i))
    
    return _max
