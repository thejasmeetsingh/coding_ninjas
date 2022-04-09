def removeLeafNodes(root):
    if not root.left and not root.right:
        del root
        return None
    
    if root.left:
        root.left = removeLeafNodes(root.left)
    if root.right:
        root.right = removeLeafNodes(root.right)
    
    return root
