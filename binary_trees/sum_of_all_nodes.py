def getSum(root):
    return getSum(root.left) + getSum(root.right) + root.data if root else 0
