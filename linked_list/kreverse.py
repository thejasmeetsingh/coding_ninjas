def kReverse(head, k):
    if not k:
        return head
	
    curr = head
    prev = None
    next = None
    count = 0
    
    while count < k and curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    
    if next:
        head.next = kReverse(next, k)
    
    return prev
