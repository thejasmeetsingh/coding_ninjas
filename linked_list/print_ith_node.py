def printIthNode(head, i):
    if not head:
        return
    
    count = 0
    node = head
    
    while node:
        if i == count:
            print(node.data)
            return
        count += 1
        node = node.next
    
    return
