import queue
import heapq


def buyTicket(arr, n, k):
    if not arr:
        return 0
    
    pq = []
    q = queue.Queue()
    
    for i in range(n):
        heapq.heappush(pq, arr[i])
        heapq._heapify_max(pq)
        q.put([i, arr[i]])
    
    time = 0
    
    while not q.empty():
        idx, data = q.get()

        if pq[0] == data:
            time += 1
            
            if idx == k:
            	return time
            
            heapq.heappop(pq)
            heapq._heapify_max(pq)
        
        if pq[0] != data:
            q.put([idx, data])
