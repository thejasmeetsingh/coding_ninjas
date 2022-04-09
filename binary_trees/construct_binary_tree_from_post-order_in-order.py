def buildTree(postOrder, inOrder, n):
    if not inOrder:
        return None
    
    node = BinaryTreeNode(postOrder[-1])
    index = inOrder.index(node.data)
    
    node.left = buildTree(postOrder[:index], inOrder[:index], n)
    node.right = buildTree(postOrder[index:-1], inOrder[index + 1:], n)
    return node
