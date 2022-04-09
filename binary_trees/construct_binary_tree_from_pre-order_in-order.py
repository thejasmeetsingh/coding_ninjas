def buildTree(preOrder, inOrder, n):
    if not inOrder:
        return
    
    root = BinaryTreeNode(preOrder[0])
    index = inOrder.index(root.data)
    
    root.left = buildTree(preOrder[1:index + 1], inOrder[:index], n)
    root.right = buildTree(preOrder[index + 1:], inOrder[index + 1:], n)
    return root
