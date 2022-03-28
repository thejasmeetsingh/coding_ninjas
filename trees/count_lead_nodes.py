def leafNodeCount(tree):
    if not tree:
        return -1
    
    total_leaf_nodes = 0
    queue = [tree]
    
    while queue:
        node = queue.pop(0)
        if len(node.children) == 0:
            total_leaf_nodes += 1
        queue.extend(node.children)
    
    return total_leaf_nodes
