def postOrder(tree):
    if not tree:
        return
    
    for child in tree.children:
        postOrder(child)
    
    print(tree.data, end=" ")
