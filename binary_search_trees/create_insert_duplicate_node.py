def insertDuplicateNode(root):
    if not root:
        return
    
    node = BinaryTreeNode(root.data)
    node.left = root.left
    root.left = node
    
    insertDuplicateNode(node.left)
    insertDuplicateNode(root.right)
