def maxDataNode(tree):
    if not tree:
        return tree
    
    node, _max = tree, tree.data
    queue = [tree]
    
    while queue:
        _node = queue.pop(0)
        if _node.data > _max:
            node = _node
            _max = _node.data
        queue.extend(_node.children)
    
    return node
