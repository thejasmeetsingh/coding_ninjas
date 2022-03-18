def findNode(head, n):
    if not head:
        return -1
    
    node = head
    count = 0
    
    while node:
        if node.data == n:
            return count
        node = node.next
        count += 1
        
    return -1
 
