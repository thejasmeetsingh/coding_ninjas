def isBST(root, left_node=None, right_node=None):
    if not root:
        return True
    
    if left_node and root.data <= left_node.data:
        return False
    
    if right_node and root.data >= right_node.data:
        return False
    
    return isBST(root.left, left_node, root) and isBST(root.right, root, right_node)
