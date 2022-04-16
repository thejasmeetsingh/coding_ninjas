def getLCAUtil(root, a, b):
    if not root:
        return None
    
    if root.data == a or root.data == b:
        return root
    
    node1 = getLCAUtil(root.left, a, b)
    node2 = getLCAUtil(root.right, a, b)
    
    if node1 and node2:
        return root
    
    return node1 if node1 else node2


def getLCA(root, a, b):
    if not root:
        return -1
    
    node = getLCAUtil(root, a, b)
    return node.data if node else -1
