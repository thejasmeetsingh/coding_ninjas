def deleteAlternateNodes(head):
    if not head:
        return head
    
    prev = None
    node = head
    idx = 0
    
    while node and node.next:
        if idx % 2 != 0:
            prev.next = node.next
        else:
            prev = node
        
        node = node.next
        idx += 1
    
    if idx % 2 != 0:
        prev.next = None
    
    return head
