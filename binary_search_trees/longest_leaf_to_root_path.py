def longestPath(root):
    if not root:
        return []
    
    right = longestPath(root.right)
    left = longestPath(root.left)
    
    if len(right) > len(left):
        right.append(root.data)
        return right
    else:
        left.append(root.data)
        return left
