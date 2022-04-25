import heapq
def kSmallest(lst, k):
    if not lst:
        return []
    
    heapq.heapify(lst)
    return heapq.nsmallest(k, lst)
