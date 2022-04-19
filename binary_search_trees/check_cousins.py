def get_level(root, x):
    q = queue.Queue()
    
    q.put([root, 1, None])
    
    while not q.empty():
        node, lvl, prev_node = q.get()
        
        if node.data == x:
            return lvl, prev_node
        
        prev_node = node
        if node.left:
            q.put([node.left, lvl + 1, node])
        if node.right:
            q.put([node.right, lvl + 1, node])
    
    return []
    

def checkCousins(root,p,q):
    if not root:
        return False
    
    level1, prev_node1 = get_level(root, p)
    level2, prev_node2 = get_level(root, q)
    
    return level1 == level2 and prev_node1.data != prev_node2.data
