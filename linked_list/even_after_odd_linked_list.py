def evenAfterOdd(head):
    if not head:
        return head
    
    odd_head, odd_tail, even_head, even_tail = None, None, None, None
    
    while head:
        if head.data % 2 == 0:
            if not even_head:
                even_head = even_tail = head
            else:
                even_tail.next = head
                even_tail = head
        else:
            if not odd_head:
                odd_head = odd_tail = head
            else:
                odd_tail.next = head
                odd_tail = head
        
        head = head.next
    
    if even_head:
        even_tail.next = None
        
    if odd_head:
        odd_tail.next = even_head
	
    return odd_head if odd_head else even_head
