def get_mid_node(head):
    if not head:
        return head
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


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


def mergeSort(head):
    if head and head.next:
        mid_node = get_mid_node(head)
        head1 = mid_node.next
        mid_node.next = None
        
        left_ll = mergeSort(head)
        right_ll = mergeSort(head1)
        
        return mergeTwoSortedLinkedLists(left_ll, right_ll)
        
    return head
