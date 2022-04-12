def findPathBST(root, data):
    if not root:
        return None
    
    result = []
    q = queue.Queue()
    q.put(root)
    
    while root:
        result.append(root.data)
        
        if data == root.data:
            return result[::-1]
        
        if root.data > data:
            root = root.left
        else:
            root = root.right
    
    return []
