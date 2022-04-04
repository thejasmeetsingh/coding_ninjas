def mirrorBinaryTree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
