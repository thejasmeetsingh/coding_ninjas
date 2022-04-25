import heapq

def kthLargest(lst, k):
    if not lst:
        return []
    heapq.heapify(lst)
    return heapq.nlargest(k, lst)[k - 1]
