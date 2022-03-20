def bubbleSort(head):
    if not head:
        return head
    
    node1 = head
    
    while node1:
        node2 = head
        while node2:
            if node2.data > node1.data:
                node1.data, node2.data = node2.data, node1.data
            node2 = node2.next
        node1 = node1.next
    
    return head
