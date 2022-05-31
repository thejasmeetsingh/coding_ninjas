def findWinner(n, x, y):
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 0
    dp[x] = 0
    dp[y] = 0
    
    for i in range(2, n + 1):
        if dp[i - 1] == 1:
            dp[i] = 0
            continue
        
        if i >= x:
            if dp[i - x] == 1:
                dp[i] = 0
                continue
        
        if i >= y:
            if dp[i - y] == 1:
                dp[i] = 0
                continue
        
        dp[i] = 1
	
    return "Beerus" if dp[n] == 0 else "Whis"
