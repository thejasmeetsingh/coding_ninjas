MOD = 1000000007

def balancedBTs(n):
    if n < 2:
        return 1
    
    a = b = 1
    c = 3
    
    for _ in range(2, n + 1):
        c = (b * b + 2 * b * a) % MOD
        a = b
        b = c
    
    return c
