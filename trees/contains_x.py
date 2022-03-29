def containsX(tree, x):
    if not tree:
        return False
    
    if tree.data == x:
        return True
    
    res = False
    
    for child in tree.children:
        _res = containsX(child, x)
        
        if res != _res and _res:
            res = _res
    
    return res
