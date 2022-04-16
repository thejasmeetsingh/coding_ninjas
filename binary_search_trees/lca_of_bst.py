def lcaInBSTUtil(root, a, b):
    if not root:
        return None
    
    if root.data == a or root.data == b:
        return root
    
    node1 = lcaInBSTUtil(root.left, a, b)
    node2 = lcaInBSTUtil(root.right, a, b)
    
    if node1 and node2:
        return root
    
    return node1 if node1 else node2


def lcaInBST(root, a, b):
    if not root:
        return -1
    
    node = lcaInBSTUtil(root, a, b)
    return node.data if node else -1
