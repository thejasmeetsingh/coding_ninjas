def checkMaxHeap(lst):
    if not lst:
        return False
    
    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            return False
    return True
