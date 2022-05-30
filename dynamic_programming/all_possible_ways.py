def allWaysUtil(x, n, num, _sum):
    res = 0
    pow = math.pow(num, n)
    
    while (pow + _sum) < x:
        res += allWaysUtil(x, n, num + 1, _sum + pow)
        num += 1
        pow = math.pow(num, n)
    
    if (pow + _sum) == x:
        res += 1
    return res
    
def allWays(x, n):
    return allWaysUtil(x, n, 1, 0)
