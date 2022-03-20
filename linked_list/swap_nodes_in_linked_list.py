def swapNodes(head, i, j):
    if not head:
        return head
    
    node = head
    idx = 0
    
    prev, prev1, curr1, prev2, curr2 = None, None, None, None, None
    
    while node:
        if idx == i:
            prev1 = prev
            curr1 = node
        
        if idx == j:
            prev2 = prev
            curr2 = node
        
        prev = node
        node = node.next
        idx += 1
    
    if prev1:
        prev1.next = curr2
    else:
        head = curr2
    
    if prev2:
        prev2.next = curr1
    else:
        head = curr1
    
    node1 = curr2.next
    curr2.next = curr1.next
    curr1.next = node1
    
    return head
