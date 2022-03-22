def reverseQueue(inputQueue):
    if inputQueue.qsize() == 0:
        return
    
    element = inputQueue.get()
    reverseQueue(inputQueue)
    inputQueue.put(element)
