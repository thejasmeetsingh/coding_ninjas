def lis(arr):
    if not arr:
        return 0
    
    dp = [0 for _ in range(len(arr))]
    dp[0] = 1
    
    for i in range(1, len(arr)):
        dp[i] = 1
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    dp.sort()
    return dp[-1]
