def skipMdeleteN(head, M, N):
    if not head or not N:
        return head
    
    if not M:
        return None
    
    curr_node = head
    count = 1
    
    while curr_node:
        if count == M:
            count = 0
            node = curr_node.next
            del_count = 0

            while node and del_count != N:
                node = node.next
                del_count += 1
            
            curr_node.next = node
        
        count += 1
        curr_node = curr_node.next
    
    return head
