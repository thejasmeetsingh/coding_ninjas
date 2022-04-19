def removeLeafNodes(root):
    if not root: 
        return None
    
    if not root.children:
        return None
    
    i = 0
    while i < len(root.children):
        child = root.children[i]
        
        if len(child.children) == 0:
            for j in range(i, len(root.children) - 1):
                root.children[j] = root.children[j + 1]
                
            root.children.pop()
            i -= 1
        i += 1

    for i in range(len(root.children)):
        root.children[i] = removeLeafNodes(root.children[i])
        
    return root
