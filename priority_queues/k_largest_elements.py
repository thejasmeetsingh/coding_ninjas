import heapq
def kLargest(lst, k):
    if not lst:
        return []
    
    heapq.heapify(lst)
    return heapq.nlargest(k, lst)
