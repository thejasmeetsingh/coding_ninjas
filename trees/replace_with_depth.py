def replacewithDepth(tree, count=0):
    if not tree:
        return
    
    tree.data = count
    
    for child in tree.children:
        replacewithDepth(child, count + 1)
