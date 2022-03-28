def sumOfAllNodes(root):
    if not root:
        return 0
    
    queue = [root]
    _sum = 0
    
    while queue:
        node = queue.pop(0)
        _sum += node.data
        queue.extend(node.children)
    
    return _sum
