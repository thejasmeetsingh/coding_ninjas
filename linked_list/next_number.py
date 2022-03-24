def reverse(head):
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
        
        

def nextNumber(head):
    if not head:
        return head
    
    head = reverse(head)
    node = head
    carry = 1
    
    while node.next and carry > 0:
        num = node.data + carry
        node.data = num % 10
        carry = num // 10
        node = node.next
    
    if carry > 0:
        num = node.data + carry
        node.data = num % 10
        node.next = Node(num // 10)
    
    return reverse(head)
