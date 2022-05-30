def waysToMakeCoinChange(denominations, numDenominations, value):
    dp = [0 for _ in range(value + 1)]
    dp[0] = 1
    
    for i in range(numDenominations):
        for j in range(denominations[i], value + 1):
            dp[j] += dp[j - denominations[i]]
    
    return dp[value]
