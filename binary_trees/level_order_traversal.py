def printLevelWise(root):
    if not root:
        return
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        for _ in range(q.qsize()):
            node = q.get()
            print(node.data, end=" ")
            
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        print()
