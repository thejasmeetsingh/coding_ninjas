def constructBST(arr):
    if not arr:
        return None
    
    index = (len(arr) - 1) // 2
    root = BinaryTreeNode(arr[index])
    
    left = constructBST(arr[:index])
    right = constructBST(arr[index + 1:])
    
    root.left = left
    root.right = right
    
    return root
