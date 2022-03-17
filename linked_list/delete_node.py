def deleteNode(head, pos):
    if not head:
        return
    
    prev_node = None
    node = head
    count = 0
    
    while node:
        if count == pos:
            if not prev_node:
                return node.next
            else:
                prev_node.next = node.next
                return head
        else:    
            count += 1
            prev_node = node
            node = node.next
    
    return head
