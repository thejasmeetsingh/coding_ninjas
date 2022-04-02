def isIdentical(tree1, tree2):
    if not tree1 and not tree2:
        return True
    
    if (tree1 and not tree2) or (not tree1 and tree2):
        return False
    
    if tree1.data != tree2.data or len(tree1.children) != len(tree2.children):
        return False
    
    i = 0
    
    while i < len(tree1.children):
        if isIdentical(tree1.children[i], tree2.children[i]):
            i += 1
        else:
        	return False
    
    return True
