def mergeTwoSortedLinkedLists(head1, head2):
    if not head1:
        return head2
    
    if not head2:
        return head1
    
    if head2.data < head1.data:
        head1, head2 = head2, head1
    
    new_head, new_tail = head1, head1
    head1 = head1.next
    
    while head1 and head2:
        if head1.data < head2.data:
            new_tail.next = head1
            new_tail = head1
            head1 = head1.next
        else:
            new_tail.next = head2
            new_tail = head2
            head2 = head2.next
	
    while head1:
        new_tail.next = head1
        new_tail = head1
        head1 = head1.next
    
    while head2:
        new_tail.next = head2
        new_tail = head2
        head2 = head2.next
    
    return new_head
