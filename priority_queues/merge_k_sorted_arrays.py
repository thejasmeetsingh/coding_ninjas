import heapq

def mergeKSortedArrays(lst):
    if not lst:
        return []
    
    heap = []
    
    for sub_arr in lst:
        for element in sub_arr:
            heapq.heappush(heap, element)
    
    result = []
    
    while heap:
        result.append(heapq.heappop(heap))
    return result
