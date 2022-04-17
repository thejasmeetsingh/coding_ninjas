def rootToLeafPathsSumToK(root, k, path=""):
    if not root:
        return
    
    if not root.left and not root.right:
        if root.data == k:
            print(path + " " + str(root.data) if path else str(root.data))
        return
    
    rootToLeafPathsSumToK(root.left, k - root.data, path + " " + str(root.data) if path else str(root.data))
    rootToLeafPathsSumToK(root.right, k - root.data, path + " " + str(root.data) if path else str(root.data))
