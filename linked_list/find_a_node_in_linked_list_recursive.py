def findNodeRec(head, n, idx=0):
    if not head:
        return -1
    
    if head.data == n:
        return idx
    
    return findNodeRec(head.next, n, idx + 1)
