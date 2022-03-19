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
