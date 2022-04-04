def height(root):
    if not root:
        return 0
    
    _height = 0
    q = queue.Queue()
    q.put([root, 1])
    
    while not q.empty():
        node, x = q.get()
        _height = max(_height, x)
        
        if node.left:
            q.put([node.left, _height + 1])
        if node.right:
            q.put([node.right, _height + 1])
    
    return _height
