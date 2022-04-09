def get_height(root):
    return max(get_height(root.left), get_height(root.right)) + 1 if root else 0

def isBalanced(root):
    return abs(get_height(root.left) - get_height(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right) if root else True
