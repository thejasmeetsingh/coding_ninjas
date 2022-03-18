def reverse_linked_list(head):
    if not head:
          return head
        
    first_node = head
    second_node = head.next
    node = None
    first_node.next = None

    while second_node:
      node = second_node.next
      second_node.next = first_node
      first_node = second_node
      second_node = node

    return first_node

    
def isPalindrome(head):
    if not head:
        return True
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    new_head = reverse_linked_list(slow)
    
    while new_head and head:
        if new_head.data != head.data:
            return False
        
        new_head = new_head.next
        head = head.next
    
    return True
