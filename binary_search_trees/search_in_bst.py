def searchInBST(root, k):
    if not root:
        return False
    
    while root:
        if root.data == k:
            return True
        
        if root.data > k:
            root = root.left
        else:
            root = root.right
    
    return False
