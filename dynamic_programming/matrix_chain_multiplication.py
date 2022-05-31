def mcm(p, n):
    n = len(p)
    dp = [[0 for __ in range(n + 1)] for _ in range((n + 1))]
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            
            k = i
            while j < n and k <= j - 1:
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j], dp[i][j])
                k = k + 1
    
    return dp[1][n - 1]
