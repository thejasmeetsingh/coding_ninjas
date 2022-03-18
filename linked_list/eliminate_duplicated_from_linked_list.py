def removeDuplicates(head):
    if not head:
        return head
    
    prev_node = head
    node = head.next
    
    while node.next:
        if prev_node.data != node.data:
            prev_node.next = node
            prev_node = node
        node = node.next
    
    if prev_node.data == node.data:
        prev_node.next = None
    
    return head
  
