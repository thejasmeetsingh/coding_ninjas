def towerOfHanoiUtil(n, src, aux, dst, result):
    if n == 0:
        return
    
    towerOfHanoiUtil(n - 1, src, dst, aux, result)
    result.append([src, dst])
    towerOfHanoiUtil(n - 1, aux, src, dst, result)
    

def towerOfHanoi(n):
    result = []
    
    if n == 0:
        return result
    
    towerOfHanoiUtil(n, 1, 2, 3, result)
    return result
