def printLevelWise(root):
    if not root:
        return
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        node = q.get()
        print("{}:L:{},R:{}".format(node.data, node.left.data if node.left else -1, node.right.data if node.right else -1))
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
