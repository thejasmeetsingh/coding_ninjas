def sortedLLFromBST(root):
    if not root:
        return
    
    head = node = None
    stack = []
    
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            
            if not node:
                head = node = Node(root.data)
            else:
                node.next = Node(root.data)
                node = node.next
            
            root = root.right
    
    return head
