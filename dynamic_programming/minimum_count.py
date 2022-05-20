def minCount(n):
    arr = []
    k = 1
    
    while k * k <= n:
        arr.append(k * k)
        k += 1
    
    dp = [maxsize for _ in range(n + 1)]
    
    dp[n] = 0
    
    for i in range(n - 1, -1, -1):
        for j in range(len(arr)):
            if i + arr[j] <= n:
                dp[i] = min(dp[i], dp[i + arr[j]])
        dp[i] += 1
    
    return dp[0]
