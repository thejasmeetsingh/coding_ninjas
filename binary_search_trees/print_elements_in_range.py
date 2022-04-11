def searchInBST(root, k):
    if not root:
        return False
    
    while root:
        if root.data == k:
            return True
        
        if root.data > k:
            root = root.left
        else:
            root = root.right
    
    return False


def elementsInRangeK1K2(root, k1, k2):
    if not root:
        return
    
    for num in range(k1, k2 + 1):
        if searchInBST(root, num):
            print(num, end=" ")
