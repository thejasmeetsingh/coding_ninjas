def preOrder(root):
    if not root:
        return
    
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)
