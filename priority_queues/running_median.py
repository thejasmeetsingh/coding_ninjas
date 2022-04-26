import heapq


def findMedian(arr, n):
    if not arr:
        return
    
    minHeap, maxHeap = [], []
    
    for element in arr:
        heapq.heappush(maxHeap, -element)
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))

        if len(minHeap) > len(maxHeap):
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        
        if len(minHeap) != len(maxHeap):
            print(-maxHeap[0], end=" ")
        else:
            print((minHeap[0] - maxHeap[0]) // 2, end=" ")
