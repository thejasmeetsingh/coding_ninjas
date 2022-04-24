class PriorityQueueNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

        
class PriorityQueue:
    def __init__(self):
        self.pq = []
        
    def isEmpty(self):
        return len(self.pq) == 0
    
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].data
    
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
    
    
    def __percolateDown(self):
        parentIndex = 0
        
        while (2 * parentIndex + 1) < self.getSize():
            childIndex = 2 * parentIndex + 1
            
            if childIndex + 1 < self.getSize() and self.pq[childIndex + 1].priority > self.pq[childIndex].priority:
                childIndex += 1
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                break
            else:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
            
            parentIndex = childIndex
    
    def insert(self, ele, priority):
        pq_node = PriorityQueueNode(ele, priority)
        self.pq.append(pq_node)
        self.__percolateUp()
        
        
    def removeMax(self):
        if self.isEmpty():
            return None
        
        self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
        element = self.pq.pop().data
        self.__percolateDown()
        return element
