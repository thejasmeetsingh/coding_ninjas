def maxMoneyLooted(houses, n):
    if not houses:
        return 0
    
    arr = [0 for _ in range(n + 1)]
    arr[0] = houses[0]
    arr[1] = max(arr[0], houses[1])
    
    for i in range(2, n):
        arr[i] = max(arr[i - 1], houses[i] + arr[i - 2])
    
    return arr[n - 1]
