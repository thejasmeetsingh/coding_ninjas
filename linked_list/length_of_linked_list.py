def length(head):
    if not head:
        return 0
    
    count = 0
    node = head
    
    while node:
        count += 1
        node = node.next
    
    return count
