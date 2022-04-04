def isNodePresent(root, x):
    if not root:
        return False
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        node = q.get()
        
        if node.data == x:
            return True
        
        if node.left:
            q.put(node.left)
        
        if node.right:
            q.put(node.right)
    
    return False
