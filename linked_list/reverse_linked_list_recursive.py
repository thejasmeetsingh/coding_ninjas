def reverseLinkedListRec(head):
    if not head or not head.next:
        return head
    
    tail = head.next
    second_head = reverseLinkedListRec(head.next)
    
    tail.next = head
    head.next = None
    return second_head
