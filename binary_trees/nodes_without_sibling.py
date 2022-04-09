def printNodesWithoutSibling(root):
    if not root:
        return
    
    if root.left and not root.right:
        print(root.left.data, end=" ")
        printNodesWithoutSibling(root.left)
    
    elif not root.left and root.right:
        print(root.right.data, end=" ")
        printNodesWithoutSibling(root.right)
    
    else:
        printNodesWithoutSibling(root.left)
        printNodesWithoutSibling(root.right)
