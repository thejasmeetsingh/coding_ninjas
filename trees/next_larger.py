def nextLargest(tree, n):
    if not tree:
        return
    
    result = None
    if tree.data > n:
        result = tree
	
    for child in tree.children:
        node = nextLargest(child, n)
        if (node and node.data > n) and ((result and node.data < result.data) or not result):
            result = node
    
    return result
