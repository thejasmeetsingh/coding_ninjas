def appendLastNToFirst(head, n):
    if not head or  not n:
        return head
    
    length = 0
    node = head
    
    while node:
        length += 1
        node = node.next
    
    idx = length - n
    node = head

    while node and idx > 1:
        idx -= 1
        node = node.next

    new_head = node.next
    node.next = None
    old_head = head
    head = new_head
    
    while new_head.next:
        new_head = new_head.next
    
    new_head.next = old_head
    
    return head
