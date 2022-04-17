def replaceWithLargerNodesSum(root, _sum=0):
    if not root:
        return _sum
    
    _sum = replaceWithLargerNodesSum(root.right, _sum)
    root.data += _sum
    _sum = replaceWithLargerNodesSum(root.left, root.data)
    return _sum
